from django.urls import path, include

from .views import swapsView

urlpatterns = [
    path('', swapsView, name='swaps'),
]
