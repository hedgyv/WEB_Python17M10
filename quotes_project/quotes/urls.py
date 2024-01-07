from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:author_id>/', views.author_detail, name='author'),
    path('add_quote/', views.new_quote_form, name = 'add_quote')
]
