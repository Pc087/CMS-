from django.urls import path
from . import views
from complaints.views import AddView
from .forms import DriverEditForm

urlpatterns = [
    path('list/', views.driver_list, name='driver_list'),
    path('detail/<work_number>/', views.driver_detail, name='driver_detail'),
    path('add/', AddView.as_view(form_class=DriverEditForm, template_name='driver_add.html'), name='driver_add'),
    path('del/', views.driver_del, name='driver_del'),
    path('search/', views.driver_search, name='driver_search'),
]