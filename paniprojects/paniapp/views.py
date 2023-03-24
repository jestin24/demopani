from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import team


def demo(request):
    obj = place.objects.all()
    return render(request, 'index.html', {'result': obj})


def demo(request):
    tm = team.objects.all()
    return render(request, 'index.html', {'result': tm})

# def addition(request):
#     return render(request,'detail.html')
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('contact details')
# def detail(request):
#     return HttpResponse('contact details')
# def thanks(request):
#     return HttpResponse('thank you')
