# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.directory import views

urlpatterns = [
    # The home page
    path('', views.index, name='directory_home'),
    path('fetch/', views.load_data, name='directory_load_data'),
    # path('post-store/', views.AnagraficaStore.as_view(), name='clienti_post_store'),
    # path('post/<int:id>/edit/', views.post_edit, name='clienti_post_edit'),
    # path('post/<int:id>/delete', views.post_delete, name='clienti_post_delete'),
]
