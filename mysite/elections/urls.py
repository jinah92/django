from django.urls import path, include
from .views import index, areas, polls

urlpatterns = [
    path('', index),
    path('areas/<str:area>/', areas),
    path('polls/<int:poll_id>/', polls)
]
