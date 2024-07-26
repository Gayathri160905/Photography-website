from django.shortcuts import render

# Create your views here.

def home(reqest):
    return render(reqest,'home.html')

def stills(reqest):
    return render(reqest,'stills.html')

def about(reqest):
    return render(reqest,'about.html')