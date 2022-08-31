from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def result(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    addi=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return render(request,"result.html",{'obj1':addi,'obj2':sub,'obj3':mul,'obj4':div})
def contact(request):
    return HttpResponse("This is My Contact Page")
def details(request):
    return HttpResponse("This is My Details page")
def thanks(request):
    return HttpResponse("Thank you")