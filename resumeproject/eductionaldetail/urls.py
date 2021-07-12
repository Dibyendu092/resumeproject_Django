from django.urls import path
from . import views
urlpatterns={
    path('educationaldetail/', views.education, name = 'education')
}