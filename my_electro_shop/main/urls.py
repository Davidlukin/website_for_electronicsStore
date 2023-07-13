from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.index, name='home'),
 path('info', views.info, name='info'),
 path('contact', views.contact, name='contact'),
 path('pickup', views.pickup, name='pickup'),
 path('delivery', views.delivery, name='delivery'),
 path('payment', views.payment, name='payment'),
 path('grade',views.grade, name='grade'),
 path('submit_form/', views.submit_form, name='submit_form'),
 path('catalog', include('for_admin.urls'), name='catalog_home'),
]