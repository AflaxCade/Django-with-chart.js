from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('linechart/', views.linechart, name='linechart'),
    path('piechart/', views.piechart, name='piechart'),
    path('doughnutchart/', views.doughnutchart, name='doughnutchart'),
]