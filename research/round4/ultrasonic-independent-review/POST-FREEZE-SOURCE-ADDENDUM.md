# Post-freeze source addendum

18 September2026. These source notes add context without changing the frozen technical protocol or pre-result review criteria. No performance result has been inspected.

Parent supplied two further primary comparisons:

- Zhuang, Zhang, Lian and Drinkwater2020: https://www.mdpi.com/1424-8220/20/17/4951 ; publisher manuscript https://research-information.bris.ac.uk/files/258439357/sensors_20_04951_v2.pdf . Its historical image-memory comparison reportedly gives26MB TFM versus1100MB wavenumber and26/43MB PWI for a400×300 image. These figures concern the implementations and hardware of that study, not a present-day lower bound or measured benefit of the candidate. The final judgment should inspect the actual experiment's optimized streamed baselines.
- EXTENDE UT Analysis: https://www.extende.com/civa-ndt-simulation-software/modules-available-in-civa/ultrasonic-testing-analysis-with-civa/ . Parent reports existing saved automation and reporting. Generic batch automation is therefore not an unexplored feature, and a numerical gain must survive the whole workflow.

Independent follow-up on TWI's primary FMC page confirms that it promotes real-time optimized TFM/Crystal, lists data volume and acquisition limits, and sells technical support. These are useful market and counterevidence; the proposed interpolation backend does not fix acquisition SNR or storage loss.

An independent retrieval of the original PMC acquisition article was met by a browser check. The target geometry statement remains traced to the researcher's inspection and published paper citation, rather than falsely described as independently re-read in this environment. No bypass attempted.

## Close numerical prior art (identified before outputs; appended after outputs)

Kruizinga, Mastik, de Jong, van der Steen and van Soest (2012), *Plane-wave ultrasound beamforming using a nonuniform fast Fourier transform*, DOI10.1109/TUFFC.2012.2509, IEEE TUFFC59(12),2684–2691. Primary bibliographic/abstract record: https://pubmed.ncbi.nlm.nih.gov/23221217/ ; author institution's thesis reproducing the paper: https://repub.eur.nl/pub/77779/150310_Kruizinga-Pieter.pdf . The abstract explicitly describes replacing frequency–wavenumber interpolation using NUFFT and evaluating computational cost, accuracy and image quality. Thus the broad numerical transfer is established. A useful modern OSS implementation may still have a practical wedge, but novelty cannot be assigned for introducing NUFFT into ultrasound.

Parent supplied Marmonier et al.2022, *Real-time 3D imaging with Fourier-domain algorithms and matrix arrays applied to NDT*, author-hosted https://www.institut-langevin.espci.fr/biblio/2022/3/16/1898/files/article1898.pdf . Parent reports discussion of NUFFT alternatives and memory. My retrieval did not produce readable text; do not describe those details as independently reverified.
