from django.urls import path
from . import views

app_name = 'sajid'

urlpatterns = [
    path('', views.index, name='home')
]
