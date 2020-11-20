from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'index.html')

def analyze(request):
	return render(request,'index.html')

# def removepunc(request):
# 	print(request.GET.get('text',"default"))
# 	return HttpResponse("hello remove")

# def capitalizefirst(request):
# 	return HttpResponse("hello capitalizefirst")

# def newlineremove(request):
# 	return HttpResponse("hello newlineremove")

# def spaceremover(request):
# 	return HttpResponse("hello spaceremover")

# def charcount(request):
# 	return HttpResponse("hello charcount")


