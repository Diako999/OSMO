from django.shortcuts import render
from .queries import *
from shroomdk import ShroomDK

sdk = ShroomDK("24e83f37-c226-4a4d-b494-c7276440ef76")
price_stats = price_stats
query_result_set = sdk.query(price_stats,
                            ttl_minutes=60,cached=True,timeout_minutes=20,retry_interval_seconds=1,page_number=1)
raw_data = query_result_set.records
data = raw_data

def pricesView(request):
    pass