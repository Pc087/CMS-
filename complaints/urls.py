from django.urls import path
from . import views


urlpatterns = [
    path('', views.complaint_list, name='index'),
    path('history/', views.history, name='history'),
    path('complaint/driverinfosearch/', views.driver_search, name='/driverinfosearch'),
    path('complaint/detail/<number>/', views.complaint_detail, name='complaint_detail'),
    path('complaint/add/', views.AddView.as_view(), name='complaint_add'),
    path('complaint/delete/', views.complaint_delete, name='complaint_del'),
    path('complaint/search/', views.all_search, name='all_search'),
]