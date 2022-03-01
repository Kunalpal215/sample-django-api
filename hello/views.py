from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def homePage(request):
    return HttpResponse("HELLO WORLD");
def nextPage(request):
    return JsonResponse({"everthing":"went perfect"});