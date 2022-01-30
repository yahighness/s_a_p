from django.shortcuts import render

def login(request):
    response = render(request, "login.html")
    return response
