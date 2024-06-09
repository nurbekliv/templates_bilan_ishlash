# views.py
from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person


def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def jadval(request):
    queryset = Person.objects.all()
    return render(request, 'jadval.html', {'queryset': queryset})
