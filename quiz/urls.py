from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
