# Author：jin
from django.conf.urls import url, include
from blg import views
urlpatterns = [
    url(r'^get_blogs/$',views.get_blogs),
    url(r'^detail/(\d+)/$', views.get_details, name='blog_get_detail'),
    ]