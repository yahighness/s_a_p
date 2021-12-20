from django.shortcuts import render


# Create your views here.
#def blog(request):
#    return render(request)
#    if request.method == "POST":
#        return render(
#            request=request,
#            template_name="blog.html",
#            context={"source": source},
#        )


#def resource(request):
#    return render(request)
#   if request.method == "GET":
#        print(Resource.objects.all())
#        # print(data.resource_id)
#        return render(
#            request=request,
#            template_name="resource.html",
#            context={"source": source},
#        )
def include(request):
    return render(request)

def home(request):
    return render(request, 'home.html')


def client(request):
    return render(request, 'client.htm')

def resource(request):
    return render(request, 'resoure.html')

def blog(request):
    return render(request, 'blog.html')