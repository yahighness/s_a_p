from django.shortcuts import render
from django.contrib.auth import authenticate

def login(request):
    response = render(request, "login.html")
    if request.method == "POST":
     user    
    return response


def create_account(request):
    response = render(request, "create_account.html")
    return response

