"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import add_product, get_all_product, get_product, delete_product, update_product
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add',views.add_product),
    # path('api/get',views.get_all_product),
    path('api/get/', views.get_product),
    path('api/del/<int:pk>', views.delete_product),
    path('api/update/<int:pk>', views.update_product),
]