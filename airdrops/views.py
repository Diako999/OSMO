from django.shortcuts import render
from .queries import *
from shroomdk import ShroomDK

sdk = ShroomDK("4a357978-d9d9-4ba7-995e-6b60fdad9051")
airdrops_stats = airdrops_stats
query_result_set = sdk.query(airdrops_stats,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
raw_data = query_result_set.records
data = raw_data

def airdropsView(request):
    labels= []
    amount_airdropped = []
    transactions =[]
    number_of_receiver= []

    for item in data:
        labels.append(item['date'])
        amount_airdropped.append(item['amount_airdropped'])
        transactions.append(item['transactions'])
        number_of_receiver.append(item['number_of_receiver'])

    context = {'amount_airdropped': amount_airdropped, 'labels': labels, 'transactions': transactions, 'number_of_receiver': number_of_receiver}
    return render(request, 'airdrops.html', context)