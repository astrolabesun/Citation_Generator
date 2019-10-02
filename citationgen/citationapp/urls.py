from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('forms/', views.fill_form, name="forms"),
    path('forms/results/', views.results, name="results"),
    path('forms/results/history/', views.history, name="history"),
]