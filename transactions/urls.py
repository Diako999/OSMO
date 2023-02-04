from django.urls import path, include

from .views import TransactionsView

urlpatterns = [
    path('', TransactionsView, name='transactions'),
]
