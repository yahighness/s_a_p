from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.genric import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from djang.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "content"]
    default = get_success_url()

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.entry.id})


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})


# Create your views here.
def blog(request):
    return render(request)
    if request.method == "POST":
        return render(
            request=request,
            template_name="blog.html",
            context={"source": source},
        )


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
