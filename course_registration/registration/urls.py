from django.contrib import admin
from django.urls import path
from registration import views

urlpatterns = [
    path('register/', views.student_registration, name='student_registration'),
    path('ajax/load-courses/', views.load_courses, name='load_courses'),
    path('success/', views.student_success, name='student_success'),
      # Fixed typo: 'view' -> 'views'
  # Fixed typo: 'view' -> 'views'
]
