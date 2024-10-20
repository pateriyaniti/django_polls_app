from rest_framework import generics, viewsets
from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

class QuestionPagination(PageNumberPagination):
    page_size = 5


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    permission_classes =  [IsAuthenticatedOrReadOnly]
    pagination_class = QuestionPagination
    
    def perform_creation(self, serializer):
        serializer.save(qwner=self.request.user)
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]