from django.urls import path, include

from .views import StakingView

urlpatterns = [
    path('', StakingView, name='staking'),
]
