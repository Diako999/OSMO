airdrops_stats = f"""
    select date_trunc('week', block_timestamp) as date,
sum(amount) as amount_airdropped,
count(distinct(tx_id)) as transactions,
count(receiver) as number_of_receiver
from osmosis.core.fact_airdrop
  where transfer_type = 'AIRDROP'
group by date, transfer_type
order by date asc

"""