from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('total_gold', views.total_gold),
    path('reset', views.reset)
]