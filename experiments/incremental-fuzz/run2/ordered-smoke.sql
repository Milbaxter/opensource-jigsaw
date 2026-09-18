{{ config(materialized='incremental', unique_key='order_id', incremental_strategy='delete+insert') }}
select order_id, event_ts, amount, ingestion_seq from {{ source('raw', 'events') }}
{% if is_incremental() %}
where event_ts > (select coalesce(max(event_ts), 0) from {{ this }})
{% endif %}
