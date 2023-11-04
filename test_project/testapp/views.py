from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, RegistrationForm,userupdateform
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import *
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

from rest_framework import generics
from .serializers import *

class ItemRetrieveView(generics.ListAPIView):
    
    queryset = city.objects.all()
    serializer_class = ItemSerializer
 
class ItemRetrieveByidView(generics.RetrieveAPIView):
    
    queryset = city.objects.all()
    serializer_class = ItemSerializer
class ItemUpdateById(generics.RetrieveUpdateAPIView):
    queryset = city.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteById(generics.RetrieveDestroyAPIView):
    queryset = city.objects.all()
    serializer_class = ItemSerializer
    
class ItemCreate(generics.CreateAPIView):
    queryset = city.objects.all()
    serializer_class = ItemSerializer

def is_admin(user):
    return user.role == 'admin'

def home_view(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'home.html', {'username':username})
@login_required()
#@user_passes_test(is_admin)
def manage_view(request):
    users = CustomUser.objects.all()
    return render(request, 'manage.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


#@csrf_protect
def register_view(request):
    try:
        if request.method == 'POST':
           form = RegistrationForm(request.POST)
           if form.is_valid():              
               form.save()
               return redirect('login')
        else:
            form = RegistrationForm()
    except Exception as e:
        print('error mohamadd',e)
    return render(request, 'register.html', {'form': form})

def update_user_View(request,id):
    user = get_object_or_404(CustomUser, id=id)  

    if request.method == 'POST':
        form = userupdateform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage')
    else:
        form = userupdateform(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})
def delete_user_View(request,id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        form = userupdateform(request.POST, instance=user)
        if form.is_valid():
            
            if str(request.user) != str(user.username):
                print('deleted')
                user.delete()
                return redirect('manage')
            else:
                print('not deleted')
                return redirect('manage')
    else:
        form = userupdateform(instance=user)

    return render(request, 'delete_user.html', {'form': form, 'user': user})


def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def change_password_view(request):
    if request.method == 'POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})