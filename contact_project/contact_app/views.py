# contacts/views.py
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib.auth import authenticate,login as dj_login,logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.serializers import serialize

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer


    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(user)
            
            return redirect("contact_list")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')
    


def logout_view(request):
    logout(request)
    return redirect('mycart')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def advance_search(request):
    column=list()
    col="email"
    for i in col.split(','):
        column.append(i)
    contacts=Contact.objects.values_list('email','first_name')      
    #contacts_data = serialize('json', contacts)
    search={
        'column':column,
        'contacts':contacts
    }
    
    
    return render(request,'search.html',search)

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'add_contact.html', {'form': form})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]