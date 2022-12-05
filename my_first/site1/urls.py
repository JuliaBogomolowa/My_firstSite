from django.urls import path
from  . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contacts/',views.contacts),
    path('about/<str:user>',views.user1),
    path('about/<str:user>/<int:age>',views.user)
]