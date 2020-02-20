from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('', views.check_db, name='check_db-page'),
]
