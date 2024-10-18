from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model =Question
        fields = ['id', 'question_text', 'pub_date', 'owner']
        
class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    q_choice =serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )
    
    class Meta:
        model = Choice
        fields =['id', 'choice_text', 'votes', 'q_choice', 'question']

# class ChoiceSerializer(serializers.ModelSerializer):
#     questionChoice = serializers.PrimaryKeyRelatedField(
#         queryset = Question.objects.all(), source='Question', write_only=True
#     )
#     class Meta:
#         model = Choice
#         fields = ['id', 'choice_text', 'votes', 'question', 'questionChoice']
        
# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True, source='choice-set')
    
#     class Meta:
#         model = Question
#         fields = ['id', 'question_text', 'pub_date', 'choices']
        
class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
    def validate_question_text(self, value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("No spam allowed in question text!")
        return value
        