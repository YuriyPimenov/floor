from django.shortcuts import render, render_to_response
import os
# Create your views here.
def index(request):
    return render_to_response('base.html')
