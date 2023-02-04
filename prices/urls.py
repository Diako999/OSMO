from django.urls import path, include

from .views import pricesView

urlpatterns = [
    path('', pricesView, name='prices'),
]
