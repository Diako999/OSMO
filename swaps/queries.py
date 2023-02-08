swaps_stats = f"""
    select date_trunc('week', block_timestamp) as date,
    count(distinct(tx_id)) as transactions,
    max(from_amount) as from_amount_max,
    max(to_amount) as to_amount_max,
    avg(from_amount) as from_amount_avg,
    avg(to_amount) as to_amount_avg
    from osmosis.core.fact_swaps
    where to_currency like '%ibc%' and from_currency = 'uosmo'
    group by date
    order by date asc
"""