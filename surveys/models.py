from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    survey_name = models.CharField(verbose_name='Название опроса', db_index=True, max_length=200)
    pub_date = models.DateTimeField()
    end_date = models.DateTimeField()
    survey_description = models.CharField(verbose_name='Описание опроса', max_length=200)


class Question(models.Model):
    survey = models.ForeignKey(Survey, verbose_name='Опрос', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    QUESTION_TYPES = [
        (1, 'Ответ текстом'),
        (2, 'Ответ с выбором одного варианта'),
        (3, 'Ответ с выбором нескольких вариантов'),
    ]
    question_type = models.IntegerField(verbose_name='Тип вопроса', choices=QUESTION_TYPES)


class Option(models.Model):
    question = models.ForeignKey(Question, verbose_name='К вопросу: ', on_delete=models.CASCADE)
    option_name = models.CharField(verbose_name='Вариант', max_length=200)


class Answer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

