# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
         
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
         
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
         


    if charcounter == "on":
        analyzed = 0
        for char in djtext:
            if char != '\0':
                analyzed = analyzed + 1
        params = {'purpose': 'Total characters are ', 'analyzed_text': analyzed}
        djtext = analyzed


    return render(request, 'analyze.html', params)


def aboutus(request):
        return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')

# def capfirst(request):
#     return HttpResponse("capitalizefirst" "<br><br> <a href='/'>home</a>")
#
# def nlr(request):
#     return HttpResponse("newlineremove")
#
# def spacer(request):
#     return HttpResponse("Space Remover")
#
# def chcount(request):
#     return HttpResponse("Character Count")
