from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.
def blog(request):
    # return render(request)
    if request.method == "POST":
        print("title:", request.POST.get("title"))
        print("subtitle:", request.POST.get("subtitle"))
        print("feedback:", request.POST.get("body"))
    return render(
        request, "blog.html",
    )


def resource(request):
    # return render(request)
    if request.method == "GET":
    #     print(Resource.objects.all())
    #     # print(data.resource_id)
        return render(request,'resource.html')
            # request=request,
            # template_name="resource.html",
            # context={"source": source},
        # )


def home(request):
    return render(request, 'home.html')


def client(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        user, created = User.objects.get_or_create(username=username, defaults={"first_name": request.POST["fname"], "last_name": request.POST["lname"]})
        if not created:
            print(f"username {username} already taken")
    return render(request, 'client.html')
