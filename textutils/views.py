# I created this file - kp
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')

    # Check Checkbox is on
    if (removepunc == "on"):
     #analyze the text
      punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
      analyzed = ""
      for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char

      param = {'purpose':'Remove Punchuations', 'analyzed_text': analyzed}
      djtext = analyzed

    if ( fullcaps =="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()

        param = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        param = {'purpose': 'Removed New Lines ', 'analyzed_text': analyzed}
        djtext = analyzed

    if ( spaceremove == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
            else:
                print("no")
            print("pre", analyzed)

        param = {'purpose': 'Remove Extra Sapce', 'analyzed_text': analyzed}


    if(spaceremove !="on" and newlineremove !="on" and fullcaps !="on" and removepunc!="on"):
        return HttpResponse("please select any operation and try again")


    return render(request, 'analyze.html', param)