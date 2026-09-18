{{ config(materialized='incremental', unique_key='order_id', incremental_strategy='delete+insert') }}
select order_id, event_ts, amount, ingestion_seq from {{ source('raw', 'events') }}
{% if is_incremental() %}
where ingestion_seq > (select coalesce(max(ingestion_seq), 0) from {{ this }})
{% endif %}
