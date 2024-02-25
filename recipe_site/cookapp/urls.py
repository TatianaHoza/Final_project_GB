from django.contrib import admin
from django.urls import path

from cookapp import views
from cookapp.views import CategoryListView, RecipeByCategoryView

app_name = 'cookapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', RecipeByCategoryView.as_view(), name='recipe-by-category'),
    path('login/', views.login_user, name='login'),
]
