from django.urls import path
from basicapp import views


urlpatterns = [
    path('list_paginated_users/', views.ListPaginated.as_view()),
    path('list_all_users/', views.ListAll.as_view())
]
