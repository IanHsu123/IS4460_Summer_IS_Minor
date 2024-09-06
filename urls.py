"""
URL configuration for group_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views
from .views import HomePage,Register,Login,Account,Admin, Permits,PermitEdit,PermitDelete,PermitDetails,PermitAdd, Vehicles,VehicleEdit,VehicleDelete,VehicleDetails,VehicleAdd, Drivers,DriverEdit,DriverDelete,DriverDetails,DriverAdd

urlpatterns = [
    path('home_page/', views.HomePage.as_view(),name='home_page'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/',views.Login.as_view(), name='login'),

    path('account/',views.Account.as_view(), name='account'),
    path('admin/',views.Admin.as_view(), name='admin'),

    path('permits/',views.Permits.as_view(), name='permits'),
    path('permit_edit/',views.PermitEdit.as_view(), name='permit_edit'),
    path('permit_edit/<int:permit_id>/',views.PermitEdit.as_view(), name='permit_edit'),
    path('permit_delete/',views.PermitDelete.as_view(), name='permit_delete'),
    path('permit_delete/<int:permit_id>/',views.PermitDelete.as_view(), name='permit_delete'),
    path('permit_details/<int:permit_id>/',views.PermitDetails.as_view(), name='permit_details'),
    path('permit_add/',views.PermitAdd.as_view(), name='permit_add'),

    path('vehicles/',views.Vehicles.as_view(), name='vehicles'),
    path('vehicle_edit/',views.VehicleEdit.as_view(), name='vehicle_edit'),
    path('vehicle_edit/<int:vehicle_id>/',views.VehicleEdit.as_view(), name='vehicle_edit'),
    path('vehicle_delete/',views.VehicleDelete.as_view(), name='vehicle_delete'),
    path('vehicle_delete/<int:vehicle_id>/',views.VehicleDelete.as_view(), name='vehicle_delete'),
    path('vehicle_details/<int:vehicle_id>/',views.VehicleDetails.as_view(), name='vehicle_details'),
    path('vehicle_add/',views.VehicleAdd.as_view(), name='vehicle_add'),
    

    path('drivers/',views.Drivers.as_view(), name='drivers'),
    path('drivers_edit/',views.DriverEdit.as_view(), name='Driver_edit'),
    path('drivers_edit/<int:driver_id>/',views.DriverEdit.as_view(), name='driver_edit'),
    path('drivers_delete/',views.DriverDelete.as_view(), name='Driver_delete'),
    path('drivers_delete/<int:driver_id>/',views.DriverDelete.as_view(), name='driver_delete'),
    path('drivers_details/<int:driver_id>/',views.DriverDetails.as_view(), name='driver_details'),
    path('drivers_add/',views.DriverAdd.as_view(), name='driver_add'),
]