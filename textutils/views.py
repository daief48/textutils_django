from django.http import HttpResponse
from django.shortcuts import  render
def index(request):
    params = {'name':'harry','place':'Mars'}
    return render(request,'index.html',params)

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    countchar = request.POST.get('countchar','off') 
    print(djtext )
    # analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$^&*_~%'''
    analyzed = ""
    print(removepunc)
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Rmoved Punctuations", "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                analyzed = analyzed + " "
        params = {"purpose": "New Line Remove", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "New Line Remove", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if(countchar == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
        analyzed += str(count)
        params = {"purpose": "New Line Remove", "analyzed_text": analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse('Error')
# def capfirst(request):
#     return HttpResponse('capfirst')
# def newlinermove(request):
#     return HttpResponse('newlinermove')
# def spaceremove(request):
#     return HttpResponse('spaceremove')
# def charcount(request):
#     return HttpResponse('charcount')