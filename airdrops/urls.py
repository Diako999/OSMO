from django.urls import path

from .views import airdropsView

urlpatterns = [
    path('', airdropsView, name='airdrops'),
]
