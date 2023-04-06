from django.http import HttpResponse
from django.shortcuts import render
from . models import trip
from . models import team
# Create your views here.
# def space(request):
#     return HttpResponse("Hello World")
# def about(request):
#     return render(request,"about.html")
# def fall(request):
#     name="india"
#     return render(request,"fall.html")

def travelo(request):
    obj =trip.objects.all()
    tea =team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':tea})