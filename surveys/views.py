from rest_framework import generics
from .serializers import SurveySerializer, QuestionSerializer, OptionSerializer, AnswerSerializer
from .models import *


"""SURVEYS"""


class SurveyCreate(generics.CreateAPIView):
    serializer_class = SurveySerializer


class SurveysViewAll(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer

    def get_queryset(self):
        return Survey.objects.filter(pk=self.kwargs['pk'])


'''QUESTIONS'''


class QuestionCreate(generics.CreateAPIView):
    serializer_class = QuestionSerializer


class QuestionViewAll(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(pk=self.kwargs['pk'])


'''OPTIONS'''


class OptionCreate(generics.CreateAPIView):
    serializer_class = OptionSerializer


class OptionViewAll(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.filter(pk=self.kwargs['pk'])


'''ANSWERS'''


class AnswerCreate(generics.CreateAPIView):
    serializer_class = AnswerSerializer
