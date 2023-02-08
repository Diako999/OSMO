from django.shortcuts import render
from django.shortcuts import render
import json
from shroomdk import ShroomDK
from django.views.generic import TemplateView
from pages.queries import *
# Create your views here.
sdk = ShroomDK("4a357978-d9d9-4ba7-995e-6b60fdad9051")
transactions_stats = transactions
query_result_set = sdk.query(transactions_stats,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
raw_data = query_result_set.records
data = raw_data
def TransactionsView(request):
     labels = []
     tx_count = []
     cum_tx =[]
     number_of_blocks =[]
     average_tps =[]
     peak_tps =[]
     total_gas_used =[]
     average_gas_used =[]
     min_gas_used =[]
     maximum_gas_used =[]
     for item in data:
          labels.append(item['date'])
          tx_count.append(item['tx_count'])
          cum_tx.append(item['cum_tx'])
          number_of_blocks.append(item['number_of_blocks'])
          average_tps.append(item['average'])
          peak_tps.append(item['peak'])
          total_gas_used.append(item['total_gas_used'])
          average_gas_used.append(item['average_gas_used'])
          min_gas_used.append(item['min_gas_used'])
          maximum_gas_used.append(item['maximum_gas_used'])

     context = {'labels': labels,
                 'tx_count': tx_count,
                 'cum_tx': cum_tx,
                  'number_of_blocks': number_of_blocks,
                  'average_tps': average_tps,
                  'peak_tps': peak_tps,
                  'total_gas_used': total_gas_used,
                  'average_gas_used': average_gas_used,
                  'min_gas_used': min_gas_used,
                  'maximum_gas_used': maximum_gas_used}
     return render(request, 'transactions.html', context)