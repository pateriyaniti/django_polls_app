from rest_framework import generics, viewsets
from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes =  [IsAuthenticatedOrReadOnly]
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]