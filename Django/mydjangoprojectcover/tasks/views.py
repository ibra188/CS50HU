from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10 )

# Create your views here.

def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "post":
        form = NewTaskForm(request.POST)
        if form.is_valid():
           task = form.cleaned_data["task"]
           request.session["task"] += [task]
           return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })   

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
