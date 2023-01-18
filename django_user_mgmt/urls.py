"""django_user_mgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 部门管理
    path('depart_list/', views.depart_list),
    path('depart_add/', views.depart_add),
    path('depart_delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),

    # 用户管理
    path('user_list/', views.user_list),
    path('user_add/', views.user_add),

    # path('user_add/form/', views.user_add_form),  form的实现当时
    path('user_add/modelform/', views.user_add_modelform),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),
]
