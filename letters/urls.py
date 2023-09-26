from django.urls import path
from . import views

urlpatterns = [
    path('', views.incoming_letter_list, name='incoming_letter_list'),

    path('incoming/add/', views.incoming_letter_create, name='incoming_letter_create'),

    path('incoming/download/<int:pk>/', views.incoming_letter_download, name='incoming_letter_download'),

    path('outgoing/<slug:slug>/', views.outgoing_letter_list, name='outgoing_letter_list'),

    path('outgoing/add/', views.outgoing_letter_create, name='outgoing_letter_create'),
    
    path('outgoing/download/<int:pk>/', views.outgoing_letter_download, name='outgoing_letter_download'),
]



    # path('outgoing/', views.outgoing_letter_list, name='outgoing_letter_list'),
