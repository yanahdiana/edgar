from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "finance_data/index.html", context)

def detail_question(request, question_id):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    question = get_object_or_404(Question, id=question_id)
    return render(request, "finance_data/detail.html", {"question": question, "latest_question_list": latest_question_list})

def results(request, question_id):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "finance_data/results.html", {"question": question, "latest_question_list":latest_question_list})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "finance_data/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("finance_data:results", args=(question.id,)))


