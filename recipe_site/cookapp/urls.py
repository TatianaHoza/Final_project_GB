from django.contrib import admin
from django.urls import path

from cookapp import views, api
from cookapp.views import CategoryListView, RecipeByCategoryView

app_name = 'cookapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>-<str:slug>/', views.category_page, name='category_page'),
    path('site/create-user/', api.CreateUser.as_view()),
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', RecipeByCategoryView.as_view(), name='recipe-by-category'),
    # path('login/', views.login_user, name='login'),
]
