from django.urls import path
from . import views
urlpatterns={
    path('achivements/', views.achivements, name = 'achivements')
}