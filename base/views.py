from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request,'index.html',context=content)

def create(request):
    return render(request,'create.html')