

from django.urls import path
from . import views

urlpatterns = [
    # 第一个参数是地址，第二个参数是响应函数
    path('', views.index,name='index'),
    path('a/', views.hello),
    path(r'article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    path('edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    path('edit/action', views.edit_action, name='edit_action')

]
