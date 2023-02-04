osmo_staking = f"""
select date_trunc('week', block_timestamp) as date,
sum(amount) as reward_amount,
currency as currency
from osmosis.core.fact_staking_rewards
where tx_succeeded = True
group by date,action,currency
order by date desc

"""


osmo_tootal_staked= f"""
select 
sum(amount) as amount_staked
from osmosis.core.fact_staking
  where currency = 'uosmo'

"""


osmo_staking_rewards = f"""
select date_trunc('week', block_timestamp) as date,
sum(amount) as reward_amount,
currency as currency
from osmosis.core.fact_staking_rewards
where tx_succeeded = True
group by date,action,currency
order by date desc
"""