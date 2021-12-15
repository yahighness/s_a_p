from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request)


def resource(request):
    return render(request)
    if request.method == "GET":
        print(Resource.objects.all())
        # print(data.resource_id)
        return render(
            request=request,
            template_name="resource.html",
            context={"source": source},
        )


def home(request):
    return render(request)


def client(request):
    return render(request)
