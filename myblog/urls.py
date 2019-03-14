"""myblog URL Configuration

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
from django.conf.urls import url

from django.urls import path, include

# 导包 因为要引用函数
import blog.views as bv

urlpatterns = [
    path('admin/', admin.site.urls),
    # 第一个参数是地址，第二个参数是响应函数
    # path('blog/', include('blog.urls', 'blog'), namespace='blog'),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),

]
