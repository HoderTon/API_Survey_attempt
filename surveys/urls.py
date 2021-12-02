from django.urls import path
from . import views

urlpatterns = [
    # Surveys
    path('survey/create/', views.SurveyCreate.as_view()),
    path('survey/view_all/', views.SurveysViewAll.as_view()),
    path('survey/update/<int:pk>/', views.SurveyUpdate.as_view()),

    # Questions
    path('question/create/', views.QuestionCreate.as_view()),
    path('question/view_all/', views.QuestionViewAll.as_view()),
    path('question/update/<int:pk>/', views.QuestionUpdate.as_view()),

    # Options
    path('option/create/', views.OptionCreate.as_view()),
    path('option/view_all/', views.OptionViewAll.as_view()),
    path('option/update/<int:pk>/', views.OptionUpdate.as_view()),

    # Answers
    path('answer/create/', views.AnswerCreate.as_view()),

]
