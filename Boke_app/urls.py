# @Time    : 18-6-11 下午2:14
# @Author  : zhangbochao
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url

from .views import index

urlpatterns = [

    url(r'^index/$', index, name='index'),

]
