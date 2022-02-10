from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from my_sap.models import Post, Profile, Tag


# Create your views here.
def blog(request):
    # return render(request)
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        feedback = request.POST.get("body")
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.create(title=title, subtitle=subtitle, body=feedback, author=profile)
        tag_names = request.POST.get("tags")
        if tag_names:
            tags = [Tag.objects.create(name=t) for t in tag_names.split(",")]
            post.tags.add(*tags)

    posts = Post.objects.all()
    context = {"posts": posts, "user_id": request.user.id}
    return render(request, "blog.html", context)


def resource(request):
    print("resource request", request)
    return render(request,'resource.html')
            

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

def edit_post(request, post_id):
    
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    response = render(request, "edit_post.html", context)
    
    if post.author.user.id != request.user.id:
        return HttpResponse(status=401)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.subtitle = request.POST["subtitle"]
        post.body = request.POST["body"]
        post.save()
        response = redirect("blog")
        
    return response

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    response = render(request, "edit_post.html", context)

    if post.author.user.id != request.user.id:
        return HttpResponse(status=401)
    
    if request.method == "POST" and request.POST["confirm_delete"] == "delete":
        post.delete()
        response = redirect("blog") 
    return response
