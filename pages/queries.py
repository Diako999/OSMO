blocks_transactions = f"""
               select count(distinct (block_id)) as blocks, sum(tx_count) as transactions from osmosis.core.fact_blocks
            """
liquidity_pools = """ select count(distinct(pool_id)) as number_of_pools from osmosis.core.dim_liquidity_pools """
total_supply =  """  select sum(amount) as total_supply from osmosis.core.fact_transfers """

transactions = f""" with
                    tx_daily as (
                    select
                         date_trunc('day', block_timestamp) as date,
                         avg(GAS_USED) as average_gas_used,
                         sum(GAS_USED) as total_gas_used,
                         count(distinct (tx_id)) as tx_count,
                         count(distinct(block_id)) as number_of_blocks,
                         tx_count / 86400 as tps_tx
                    from
                         osmosis.core.fact_transactions
                    group by
                         1
                    )
                    SELECT
                    *,
                    sum(tx_count) over (
                    order by
                         date asc rows between unbounded preceding
                         and current row
                    ) as cum_TX
                    from (
                    SELECT
                         date_trunc('week', date) as date,
                         sum(tx_count) as tx_count,
                         avg(tps_tx) as "Average",
                         max(tps_tx) as "Peak",
                         sum(total_gas_used) as total_gas_used,
                         avg(average_gas_used) as average_gas_used,
                         min(average_gas_used) as min_gas_used,
                         max(average_gas_used) as maximum_gas_used,
                         median(average_gas_used) as mid_gas_used,
                    sum(number_of_blocks) as number_of_blocks
                    FROM tx_daily group by 1
                    )
          """