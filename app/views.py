from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here
def insert_topic(request):
    TFEO = TopicForm()
    d = {'TFEO':TFEO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse(str(TFDO.cleaned_data))

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFEO = WebPageForm()
    d1 = {'WFEO': WFEO}
    if request.method == 'POST':
        WFDO = WebPageForm(request.POST)
        if WFDO.is_valid():
           # WFDO.save()
            return HttpResponse(str(WFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_webpage.html',d1)

