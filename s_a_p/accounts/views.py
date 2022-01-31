from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    response = render(request, "login.html")
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password']) 
        if user is not None:
            auth_login(request, user)
            response = redirect('home')
    return response


def create_account(request):
    response = render(request, "create_account.html")
    return response

