from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

# Create your views here.

def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out')
    return redirect(request, 'logged_out.html')


# def register(request):
#
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data ['last_name']
#             user = authenticate(request, username=username, password=password,
#                                 first_name=first_name, last_name=last_name)
#             login(request, user)
#             messages.success(request, 'Hi {username}, you have successfully registered!!!')
#             return redirect('quote:quotes')
#         else:
#             messages.error(request, 'Something went wrong!!!')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})




class RegisterView(generic.CreateView):

    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('quote:quotes')
