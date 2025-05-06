from django import forms
from .models import Contact, Book
from django.forms import ModelForm


from django import forms

class ContactForm(forms.ModelForm):
    
    class Meta:
        
        model = Contact
    
        fields = ['name', 'email', 'subject']
        
        
    


class BookForm(forms.ModelForm):
    
    class Meta:
        
        model = Book
        
        fields = ['name', 'email', 'service', 'message']

