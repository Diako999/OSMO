from django.shortcuts import render
import json
from shroomdk import ShroomDK
from django.views.generic import TemplateView
from .queries import *
# Create your views here.

sdk = ShroomDK("4a357978-d9d9-4ba7-995e-6b60fdad9051")
def HomeView(request):
     sql = blocks_transactions
     pools = liquidity_pools
     supply = total_supply
     pools_result = sdk.query(pools)
     supply_result = sdk.query(supply)
     query_result_set = sdk.query(sql)
     raw_data = query_result_set.records
     data = raw_data[0]
     raw_data_pools = pools_result.records
     raw_data_supply = supply_result.records
     pools_data = raw_data_pools[0]
     supply_data = raw_data_supply[0]
     context = {
          'blocks':"{:,}".format(data['blocks']),
          'transactions': "{:,}".format(data['transactions']),
          'num_of_pools': "{:,}".format(pools_data['number_of_pools']),
          'supply': "{:,}".format(supply_data['total_supply'])
     }
     return render(request, 'index.html', context)