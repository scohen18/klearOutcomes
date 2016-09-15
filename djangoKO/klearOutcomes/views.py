from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {}

	context["input"] = "hello"

	return render(request,"klearOutcomes/index.html", context=context)



def bob(request):
	return HttpResponse("bob says hey there world!")
