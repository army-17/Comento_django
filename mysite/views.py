from django.shortcuts import render
from django.http import HttpResponse
from .models import MainContent

# Create your views here.

def index(request):

    content_list = MainContent.objects.order_by('-pub_date')  #- 붙이면 역순으로
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)