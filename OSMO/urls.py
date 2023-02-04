from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('transactions/', include('transactions.urls')),
    path('staking/', include('staking.urls')),
    path('swaps/', include('swaps.urls')),
    path('airdrops/', include('airdrops.urls')),
    path('prices/', include('prices.urls')),
]
