from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/list/', views.account_list, name='account_list'),
    path('account/add/', views.account_add, name='account_add'),
    path('account/delete/', views.account_delete, name='account_delete'),
    path('account/detail/<int:rowid>/', views.account_detail, name='account_detail'),
]