from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def list(request):
    context = {
      "name": "Book List",
    }
    return render(request, 'book/list.html', context)