from django.http.response import HttpResponse
from django.shortcuts import render

def post(request):
    return render(request, 'post/post.html')

def post1(request):
    return HttpResponse("Post1")

def post2(request):
    return HttpResponse("Post2")