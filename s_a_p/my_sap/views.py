from django.shortcuts import render

# Create your views here.
def blog(request):
    # return render(request)
    if request.method == "GET":
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
    return render(request, 'client.html')
