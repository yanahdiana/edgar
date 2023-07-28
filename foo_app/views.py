from django.shortcuts import render
from finance_data.models import Question, Choice


# Create your views here.
def index(request):
   query = request.GET.get("q","")
   if query is not None:
      question_results = Question.objects.filter(question_text__icontains=query)
      choice_results = Choice.objects.filter(choice_text__icontains=query)
   print(locals())
   return render(request, "foo_app/index.html", locals())
      
  

   
 


