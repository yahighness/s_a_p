from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

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
    if request.method == "POST":
        username = request.POST["username"]
        user, created = User.objects.get_or_create(username=username, defaults={"first_name": request.POST["first_name"], "last_name": request.POST["last_name"], "email": request.POST['email']})
        if created:
            user.set_password(request.POST['password'])
            user.save()
        response = redirect('login')
    return response

