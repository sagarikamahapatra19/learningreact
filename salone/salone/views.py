from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from contact.models import Appointment, Contact

# Auth Views

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username  # username based authenticate
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'LogIn.html', {'error': 'Invalid email or password'})
    return render(request, 'LogIn.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('index')
    return render(request, 'signup.html')


def logout_view(request):
    auth_logout(request)
    return redirect('index')

# Website Pages (Login Required)
@login_required(login_url='LogIn')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='LogIn')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='LogIn')
def service(request):
    return render(request, 'service.html')

@login_required(login_url='LogIn')
def gallery(request):
    return render(request, 'gallery.html')

def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        message = request.POST.get("message", "")
        professional = request.POST.get("professional")

        Appointment.objects.create(
            name=name, email=email, phone=phone, date=date,
            message=message, professional=professional
        )
        return render(request, "Bookingpage.html", {"success": True})

    return render(request, "Bookingpage.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)
        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")



@login_required(login_url='LogIn')
def beautyblog(request):
    return render(request, 'BeautyBlog.html')

@login_required(login_url='LogIn')
def logout_page_render(request):
    return render(request, 'LogOut.html')

