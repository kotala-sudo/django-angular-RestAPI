from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from .models import Question, Answer
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
