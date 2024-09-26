-- staging customer data

with customer_data as (
    select *
    from {{ source('raw', 'customers') }}  -- This pulls data from the raw.customers source
)

select *
from customer_data
