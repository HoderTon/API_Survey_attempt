from rest_framework import serializers
from .models import Survey, Question, Option, Answer


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
