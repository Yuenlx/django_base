from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def list(request):
    context = {
      "name": "Book List",
    }
    return render(request, 'book/list.html', context)

def create(request):
  BookInfo.objects.create(
    name="三国演义",
    pub_date="2026-01-01",
    readcount=100,
    commentcount=100,
    is_delete=False
    )
    return HttpResponse("创建成功")
 
 def update(request):
  BookInfo.objects.filter(id=1).update(name="三国演义2")
  return HttpResponse("更新成功")

def delete(request):
  BookInfo.objects.filter(id=1).delete()