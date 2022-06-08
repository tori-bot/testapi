from django.urls import path
from . import views

urlpatterns = [
    path('api/merch/',  views.MerchList.as_view()),
]