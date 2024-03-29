"""tito-taco-shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
import django_cas_ng.views
from . import views

urlpatterns = [
    path('account/login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('account/logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('admin/', admin.site.urls),
    # path('slack/', include('django_slack_oauth.urls')),
    path('integration/', include('integration.urls')),
    path('', views.index, name='home-page'),
    path('products/', include('products.urls')),
]
