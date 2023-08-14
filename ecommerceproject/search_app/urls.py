from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('', views.Search_Result, name='Search_Result'),
]