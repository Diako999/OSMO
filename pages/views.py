from django.shortcuts import render
from shroomdk import ShroomDK
from django.views.generic import TemplateView
# Create your views here.


def HomeView(request):
     data = []
     sdk = ShroomDK("24e83f37-c226-4a4d-b494-c7276440ef76")
     sql = f"""
               select
               count(distinct (author)) as developers
               from
               near.beta.github_activity
            """
     query_result_set = sdk.query(sql)
     data.append(query_result_set.records)
     context ={
          'data': data
     }
     return render(request, 'index.html', context)