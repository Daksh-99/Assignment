from .views import *
from django.urls import path

urlpatterns = [
    path('classes/', ClassList.as_view()),
    path('classes/<int:class_id>/', ClassDetail.as_view()),

    path('assignments/', AssignmentList.as_view()),
    path('assignments/<int:assignment_id>/', AssignmentDetail.as_view()),

    path('questions/', QuestionList.as_view()),
    path('questions/<int:question_id>/', QuestionDetail.as_view()),
]