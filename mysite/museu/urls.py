from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('check_db/', views.check_db, name='check_db-page'),
]
