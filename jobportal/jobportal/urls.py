"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from jobs import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
schema_view = get_swagger_view(title='Jobportal API functionality testing using swagger')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hydjobs/', views.hydjobs1),
    path('blorejobs/', views.blorejobs1),
    path('punejobs/', views.punejobs1),
    path('chennaijobs/', views.chennaijobs1),
    path('api/', include('jobs.api.urls')),
    path('swagger/',schema_view),
    path('auth-jwt/', obtain_jwt_token),
    path('auth-jwt-refresh/', refresh_jwt_token),
    path('auth-jwt-verify/', verify_jwt_token),

]
