from django.shortcuts import render
from .queries import *
from shroomdk import ShroomDK

sdk = ShroomDK("4a357978-d9d9-4ba7-995e-6b60fdad9051")
osmo_staking = weekly_staking_stats
staking_reward = osmo_staking_rewards
query_result_set = sdk.query(osmo_staking,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
query_result_set2 = sdk.query(staking_reward,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
raw_data = query_result_set.records
raw_data_reward = query_result_set2.records
rewards_result = raw_data_reward
data = raw_data
# Create your views here.
def StakingView(request):
    labels = []
    transactions = []
    action = []
    for item in data:
        labels.append(item['date'])
        transactions.append(item['transactions'])
        action.append(item['action'])

    date =[]
    reward_amount = []
    currency =[]
    for item in rewards_result:
        date.append(item['date'])
        reward_amount.append(item['reward_amount'])
        currency.append(item['currency'])
    context = {'labels': labels, 'transactions': transactions, 'action':action, 'date': date, 'reward_amount': reward_amount, 'currency': currency}

    return render(request, 'stakings.html', context)