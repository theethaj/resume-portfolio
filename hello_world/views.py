from django.shortcuts import render
from .forms import ContactForm


def hello_world(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context = {'form': form}
    else:
        context = {'form': form}
    return render(request, 'hello_world.html', context)
