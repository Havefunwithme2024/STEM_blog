from django.urls import path
from . import views

urlpatterns = [
    path('show/tariff/list/', views.tariff_plan_view, name='tariff_plan_page'),
    path('success/', views.success_view, name='success_page'),
    path('cancel/', views.cancel_view, name='cancel_page'),
    path('pay/<int:pk_tariff>/', views.pay_activate, name='pay_active')


]