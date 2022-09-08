# Created this file by meee

from string import punctuation
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse(' <a href="/">back</a> <br>   Hello About')



def analyze(request):

    djtext = (request.POST.get('text', 'default'))
    removepunc = request.POST.get('removepunc', 'default')
    upperorlower = request.POST.get('upperorlower', 'default')
    removespace = request.POST.get('removespace', 'default')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    else:
        analyzed = djtext
    
    analyzed2 = ""
    if upperorlower == "on":
        for char1 in analyzed:
            analyzed2 = analyzed2 + char1.upper()
    else:
        analyzed2 = analyzed

    final = ""
    if removespace == "on":
        for char in analyzed2:
            if char != " ":
                final = final + char
    else:
        final = analyzed2
    

    


    params = {'analyzed_text': final}
    return render(request, 'analyze.html', params)


def ex1(request):
    return render(request, 'ex1.html')
