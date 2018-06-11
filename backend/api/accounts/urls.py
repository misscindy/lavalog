# coding=UTF-8

"""
Created on 6/10/18

@author: 'bingxinfan'
"""

from django.urls import re_path

from api.accounts import views


urlpatterns = [
    re_path(r'fetch_sth/(?P<word>\w+)$', views.fetch_sth_view,
            name='api_fetch_sth'),
]

