"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from content.views import 

urlpatterns = [
	path('add_cart_view/', add_cart_view),
	path('client_home_view/', client_home_view),
	path('dispatch_home_view/', dispatch_home_view),
	path('order_success_view/', order_success_view),
	path('confirm_order_view/', confirm_order_view),
	path('admin/', admin.site.urls),
]
