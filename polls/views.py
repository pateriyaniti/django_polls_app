#from django.http import HttpResponse # type: ignore

#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")

#class Base approch
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse 
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required #decorato to ensure user is logged in 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return redirect('polls:thanks')
    else:
        form = ContactForm()
    return render(request, 'polls/contact.html', {'form': form})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    Question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice. ",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    