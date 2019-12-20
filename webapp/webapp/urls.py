"""webapp URL Configuration

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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from tours.views import TourView
from employees.views import ApprovingManagerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("tours/", TourView.as_view(), name="tours"),
    path("approving_managers/", ApprovingManagerView.as_view(), name="approving_managers")
]
