with staged_customers as (
    select * from {{ ref('stg_customers') }}
)
select
    id,
    name,
    email,
    city
from staged_customersO
