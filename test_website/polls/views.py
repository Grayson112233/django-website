from django.http import HttpResponse
from django.shortcuts import render
from .models import Question 

# This method will handle responses to the index page
def index(request):
    # List 5 most recent posts delineated by a comma
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_questions': latest_questions }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    context = { 'question': question }
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    return HttpResponse("This is the results of question " + str(question_id))

def vote(request, question_id):
    return HttpResponse("This is the voting page of question " + str(question_id))
