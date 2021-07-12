from django.urls import path
from . import views
urlpatterns={
    path('contactu/', views.contactus, name = 'contactus')
}