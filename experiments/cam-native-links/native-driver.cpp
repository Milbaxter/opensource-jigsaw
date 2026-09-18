// SPDX-License-Identifier: LGPL-2.1-or-later
// Research harness linking FreeCAD LGPL code; upstream notices retained by source fetch.
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include "prepared/Adaptive.hpp"

namespace AdaptivePath {
std::ofstream camTrace;
std::size_t camTraceIndex = 0;
void writePoint(std::ostream& f, const IntPoint& p) { f << '[' << p.X << ',' << p.Y << ']'; }
void writePath(std::ostream& f, const Path& p) {
    f << '['; bool first=true;
    for (const auto& v:p) { if(!first)f<<',';first=false;writePoint(f,v); } f<<']';
}
void writePaths(std::ostream& f, const Paths& paths) {
    f << '['; bool first=true;
    for(const auto& p:paths){if(!first)f<<',';first=false;writePath(f,p);}f<<']';
}
void writeZPath(std::ostream& f,const Path& p) { f<<'[';bool first=true;for(const auto& v:p){if(!first)f<<',';first=false;f<<v.Z;}f<<']'; }
void writeZPaths(std::ostream& f,const Paths& p) { f<<'[';bool first=true;for(const auto& v:p){if(!first)f<<',';first=false;writeZPath(f,v);}f<<']'; }
void CamTraceBegin(const IntPoint& a,const IntPoint& b,const Paths& stock,long radius,
                   double step,long scale,double ratio) {
    if (++camTraceIndex > 10000) throw std::runtime_error("trace record cap");
    camTrace << "{\"event\":\"begin\",\"index\":" << camTraceIndex
      << ",\"radius\":" << radius << ",\"stepover\":" << step << ",\"scale\":" << scale
      << ",\"ratio\":" << ratio << ",\"start\":";writePoint(camTrace,a);
    camTrace<<",\"end\":";writePoint(camTrace,b);camTrace<<",\"start_z\":"<<a.Z<<",\"end_z\":"<<b.Z<<",\"cleared\":";writePaths(camTrace,stock);
    camTrace<<",\"cleared_z\":";writeZPaths(camTrace,stock);
    camTrace<<"}\n";camTrace.flush();
    if(!camTrace || camTrace.tellp()>64*1024*1024)throw std::runtime_error("trace byte cap or write failure");
}
void CamTraceEnd(bool ok,const Path& path) {
    camTrace<<"{\"event\":\"end\",\"index\":"<<camTraceIndex<<",\"success\":"<<(ok?"true":"false")<<",\"path\":";
    writePath(camTrace,path);camTrace<<",\"path_z\":";writeZPath(camTrace,path);camTrace<<"}\n";camTrace.flush();
    if(!camTrace || camTrace.tellp()>64*1024*1024)throw std::runtime_error("trace byte cap or write failure");
}
}
#ifdef CAM_CAPTURE
#include "prepared/Adaptive-instrumented.cpp"
#else
#include "prepared/Adaptive-original.cpp"
#endif
#include "prepared/inputs.hpp"
using namespace AdaptivePath;
using Clock=std::chrono::steady_clock;

struct Request { long radius,scale; double step,ratio; IntPoint start,end; Paths stock; };
Paths readPaths(std::istream& f) {
    long nr;f>>nr;if(!f || nr<0 || nr>10000)throw std::runtime_error("invalid ring count");
    Paths out;std::size_t total=0;
    for(long i=0;i<nr;i++){
      long n;f>>n;if(!f || n<1 || n>100000 || (total+=n)>1000000)throw std::runtime_error("invalid vertex count");
      Path p;for(long j=0;j<n;j++){IntPoint q;f>>q.X>>q.Y>>q.Z;if(!f)throw std::runtime_error("invalid point");p.push_back(q);}out.push_back(p);
    }return out;
}
Request readRequest(const char* name){
    std::ifstream f(name);Request r;f>>r.radius>>r.scale>>r.step>>r.ratio>>r.start.X>>r.start.Y>>r.start.Z>>r.end.X>>r.end.Y>>r.end.Z;
    if(!f || r.radius<=0 || r.scale<=0 || !std::isfinite(r.step) || r.step<=0 || !std::isfinite(r.ratio) || r.ratio<1)
        throw std::runtime_error("invalid request state");
    r.stock=readPaths(f);std::string extra;if(f>>extra)throw std::runtime_error("trailing input");return r;
}
Adaptive2d configureRequest(const Request& r){
    Adaptive2d a;a.toolRadiusScaled=r.radius;a.scaleFactor=r.scale;a.stepOverScaled=r.step;
    a.keepToolDownDistRatio=r.ratio;a.stopProcessing=false;return a;
}
double nativeClearance(const Request& r){
    const double d=std::sqrt(DistanceSqrd(r.start,r.end));return 2*r.step>d/2?0:r.step;
}
void writeOutput(std::ostream& f,const std::list<AdaptiveOutput>& results){
 f<<'[';bool first=true;
 for(const auto& r:results){
  if(!first)f<<',';first=false;
  const bool error=r.StartPointNotFound || r.LeadPathFailed || r.UnexpectedRotateIterations || r.TooManyFailedEngagements || r.UnclearedAreaRemains || r.FailedToSetUpFinishingPass || r.FinishingLeadInFailed;
  f<<"{\"errors\":["<<r.StartPointNotFound<<','<<r.LeadPathFailed<<','<<r.UnexpectedRotateIterations<<','<<r.TooManyFailedEngagements<<','<<r.UnclearedAreaRemains<<','<<r.FailedToSetUpFinishingPass<<','<<r.FinishingLeadInFailed<<']';
  // Native early error returns can leave scalar output fields uninitialized. Never read them.
  if(!error)f<<",\"helix\":["<<r.HelixCenterPoint.first<<','<<r.HelixCenterPoint.second<<"],\"start\":["<<r.StartPoint.first<<','<<r.StartPoint.second
   <<"],\"return_motion\":"<<r.ReturnMotionType<<",\"area\":"<<r.ClearedArea<<",\"scale\":"<<r.clipperScale;
  f<<",\"paths\":[";
  bool fp=true;for(const auto& p:r.AdaptivePaths){if(!fp)f<<',';fp=false;f<<'['<<p.first<<",[";bool fv=true;
   for(const auto& v:p.second){if(!fv)f<<',';fv=false;f<<'['<<v.first<<','<<v.second<<']';}f<<"]]";
  }f<<"]}";
 }f<<']';
}
int main(int argc,char**argv){
 try{
  if(argc<4)throw std::runtime_error("run INDEX OUT | replay REQUEST OUT | geometry REQUEST OUT | verify REQUEST OUT PATH");
  const std::string mode=argv[1];std::ofstream out(argv[3]);if(!out)throw std::runtime_error("output open failed");
  out<<std::setprecision(17);camTrace<<std::setprecision(17);
  if(mode=="run"){
   int index=std::stoi(argv[2]);if(index<0 || index>=int(workloads.size()))throw std::runtime_error("bad workload");
   const auto& w=workloads[index];
#ifdef CAM_CAPTURE
   camTrace.open(std::string(argv[3])+".trace.jsonl");if(!camTrace)throw std::runtime_error("trace open failed");
#endif
   Adaptive2d a;a.toolDiameter=5;a.tolerance=.1;a.stockToLeave=0;a.forceInsideOut=false;a.finishingProfile=false;
   a.keepToolDownDistRatio=3;a.opType=otClearingInside;a.stepOverFactor=w.stepover;
   a.helixRampTargetDiameter=0;a.helixRampMinDiameter=0;a.stopProcessing=false;
   const auto t=Clock::now();const auto cpu=std::clock();
   const auto results=a.Execute(w.stock,w.paths,{},[](TPaths){return false;});
   const auto cput=double(std::clock()-cpu)/CLOCKS_PER_SEC;
   const double wall=std::chrono::duration<double>(Clock::now()-t).count();
   out<<"{\"workload\":\""<<w.id<<"\",\"wall_seconds\":"<<wall<<",\"cpu_seconds\":"<<cput<<",\"results\":";
   writeOutput(out,results);out<<"}\n";
  }else{
   const auto r=readRequest(argv[2]);auto a=configureRequest(r);ClearedArea cleared(r.radius);cleared.SetClearedPaths(r.stock);
   if(mode=="replay"){
    out<<"{\"repeats\":[";
    for(int i=0;i<3;i++){
     if(i)out<<',';auto fresh=configureRequest(r);ClearedArea c(r.radius);c.SetClearedPaths(r.stock);Path path;
     const auto t=Clock::now();const auto cpu=std::clock();bool ok=fresh.ResolveLinkPath(r.start,r.end,c,path);
     const auto cput=double(std::clock()-cpu)/CLOCKS_PER_SEC;const double wall=std::chrono::duration<double>(Clock::now()-t).count();
     out<<"{\"success\":"<<(ok?"true":"false")<<",\"wall_seconds\":"<<wall<<",\"cpu_seconds\":"<<cput<<",\"path\":";writePath(out,path);out<<",\"path_z\":";writeZPath(out,path);out<<'}';
    }out<<"]}\n";
   }else if(mode=="geometry"){
    double clearance=nativeClearance(r);ClipperOffset offset(2,.25);offset.AddPaths(r.stock,jtRound,etClosedPolygon);Paths eroded;offset.Execute(eroded,-(r.radius+clearance+2));
    const bool ep1=a.IsClearPath(Path{r.start},cleared,clearance),ep2=a.IsClearPath(Path{r.end},cleared,clearance);
    out<<"{\"clearance\":"<<clearance<<",\"endpoint_native\":["<<ep1<<','<<ep2<<"],\"center_paths\":";writePaths(out,eroded);out<<"}\n";
   }else if(mode=="verify"){
    if(argc!=5)throw std::runtime_error("verify requires path file");std::ifstream f(argv[4]);auto p=readPaths(f);if(p.size()!=1)throw std::runtime_error("one path required");
    bool ok=a.IsClearPath(p[0],cleared,nativeClearance(r));out<<"{\"native_full_path_clear\":"<<(ok?"true":"false")<<"}\n";
   }else throw std::runtime_error("unknown mode");
  }
  if(!out)throw std::runtime_error("output write failed");return 0;
 }catch(const std::exception& e){std::cerr<<"ERROR: "<<e.what()<<'\n';return 2;}
}
