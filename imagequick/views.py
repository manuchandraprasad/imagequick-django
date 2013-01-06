from base.models import *
from django.shortcuts import render, get_object_or_404

def index(request):
    """
        Provides the basic homapage for all those who are not logged in
    """
    formats = Format.objects.all()
    frequency = Frequency.objects.all()
    return render(request,'index.html',{'formats':formats,'frequencies':frequency})