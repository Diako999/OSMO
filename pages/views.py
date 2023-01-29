from django.shortcuts import render
import json
from shroomdk import ShroomDK
from django.views.generic import TemplateView
# Create your views here.


def HomeView(request):
     
     sdk = ShroomDK("24e83f37-c226-4a4d-b494-c7276440ef76")
     sql = f"""
               select count(distinct (block_id)) as blocks, sum(tx_count) as transactions from osmosis.core.fact_blocks
            """
     pools = """ select count(distinct(pool_id)) as number_of_pools from osmosis.core.dim_liquidity_pools """
     supply = """  select sum(amount) as total_supply from osmosis.core.fact_transfers """
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