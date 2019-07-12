from django.shortcuts import render, redirect
from .forms import RegisterForm

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello This is the first step to Startup!")

# def SignUpView(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return redirect("index")
#     else:
#         form = RegisterForm()
#     return render(request, 'signup.html', { 'form': form })

def ServiceView(request):
    return render(request, "services.html")

def ProjectView(request):
    return render(request, "projects.html")

def ContactView(request):
    return render(request, "contact.html")

def AboutView(request):
    return render(request, "about.html")

def IndexView(request):
    return render(request, "index.html")
