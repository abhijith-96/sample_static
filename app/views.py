from django.shortcuts import render

# Create your views here.


def samplestatic(request):
    return render(request, 'samplestatic.html')
