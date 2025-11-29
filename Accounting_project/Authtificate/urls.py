
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # path('', views.home),
    # path("api/hello", views.vApi), 
    path("wellcome", views.wellcome, name="wellcome"),
    path("", RedirectView.as_view(pattern_name = "wellcome")),
    
]