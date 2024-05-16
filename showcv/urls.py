from django.urls import path
from .views import showcv_view
urlpatterns = [
    path('',showcv_view, name='showcv'),
]