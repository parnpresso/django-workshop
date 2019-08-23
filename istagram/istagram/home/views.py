from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden

def home(request):
    extra_data = {"price": 3000}
    return render(request, "home.html", context = extra_data)
