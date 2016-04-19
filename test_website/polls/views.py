from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Question, Choice

# This method will handle responses to the index page
def index(request):
	# List 5 most recent posts delineated by a comma
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	context = { 'latest_questions': latest_questions }
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = { 'question': question }
	return render(request, "polls/detail.html", context)

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = { 'question': question }
	return render(request, "polls/results.html", context)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "No choice was selected"
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
