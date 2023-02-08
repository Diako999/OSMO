from django.shortcuts import render
from .queries import *
from shroomdk import ShroomDK

sdk = ShroomDK("4a357978-d9d9-4ba7-995e-6b60fdad9051")
swaps_stats = swaps_stats
query_result_set = sdk.query(swaps_stats,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
raw_data = query_result_set.records
data = raw_data

def swapsView(request):
    labels =[]
    transactions =[]
    from_amount_max = []
    to_amount_max = []
    from_amount_avg =[]
    to_amount_avg= []

    for item in data:
        labels.append(item['date'])
        transactions.append(item['transactions'])
        from_amount_max.append(item['from_amount_max'])
        to_amount_max.append(item['to_amount_max'])
        from_amount_avg.append(item['from_amount_avg'])
        to_amount_avg.append(item['to_amount_avg'])

    context ={
        'labels': labels,
        'transactions': transactions,
        'from_amount_max': from_amount_max,
        'to_amount_max': to_amount_max,
        'from_amount_avg': from_amount_avg,
        'to_amount_avg': to_amount_avg
    }
    return render(request, 'swaps.html', context)