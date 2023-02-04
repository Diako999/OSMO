from django.urls import path, include

from .views import airdropsView

urlpatterns = [
    path('', airdropsView, name='airdrops'),
]
