from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.All_ProdCat, name='All_ProdCat'),
    path('<slug:c_slug>/', views.All_ProdCat, name='Products_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Pro_Detail, name='Products_Category_Detail'),
]
