{{ config(materialized='incremental', unique_key='order_id', incremental_strategy='append') }}
select order_id, event_ts, amount, ingestion_seq from {{ source('raw', 'events') }}
