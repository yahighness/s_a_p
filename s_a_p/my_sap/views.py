from django.shortcuts import render

from django.contrib.auth.models import User
from my_sap.models import Post, Profile

# Create your views here.
def blog(request):
    # return render(request)
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        feedback = request.POST.get("body")
        username = request.POST["username"]
        profile = Profile.objects.get(user__username=username)
        feedback_post = Post.objects.create(title=title, subtitle=subtitle, body=feedback, author=profile)
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog.html", context)


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
        bio = request.POST["bio"]
        profile, created = Profile.objects.get_or_create(user=user, defaults={"bio": bio})  
            
    return render(request, 'client.html')
