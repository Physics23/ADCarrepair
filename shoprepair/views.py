from django.shortcuts import render, redirect
from .forms import ContactForm, BookForm
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, 'shoprepair/index.html')



def about (request):
    return render(request, 'shoprepair/about.html')


def contact(request):
    
    form = ContactForm()
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
           
        return render(request, 'shoprepair/contact.html', {'form':form})





def services(request):
    
    form = BookForm()
    
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
        
           
    return render(request, 'shoprepair/services.html', {'form':form})
