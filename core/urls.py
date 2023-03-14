from django.contrib import admin
from django.urls import path
from api.views import add_product, get_all_product, get_product, delete_product, update_product
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add',views.add_product),
    # path('api/get',views.get_all_product),
    path('api/get-product/', views.get_product),
    path('api/get/', views.get_by_ram),
    path('api/get/model/<str:model>'),
    path('api/get/model/<int:pk>')
]