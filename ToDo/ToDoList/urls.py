from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('crossOff/<list_id>', views.crossOff, name='crossOff'),
    path('edit/<list_id>', views.edit, name='edit'),
]
