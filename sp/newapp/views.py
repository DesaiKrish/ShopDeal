from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import User, Seller

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Authenticate user
        user = authenticate(request, email=email, password=password, role=role)

        if user is not None:
            # User authentication successful, login user
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
        else:
            # Authentication failed
            error = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def signup(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        role = request.POST.get('role')

        # existing_cust = None
        # existing_seller = None

        # if role == 'Customer':
        #     existing_cust = User.objects.filter(email=email).first()
        # elif role == 'Seller':
        #     existing_seller = Seller.objects.filter(email=email).first()

        data = User.objects.create(first_name=fname, last_name=lname, email=email, password=password,address=address,phone_num=contact)
        data.save()
        
        # if existing_cust or existing_seller:
        #     data['error'] = "User is already exist in System."
        #     return render(request, 'login.html', data)

        # if len(password)<8:
        #     data['error'] = "Password is too short."
        #     return render(request, 'login.html', data)

        # if len(contact)!=10:
        #     data['error'] = "Enter valid digits of Phone Number."
        #     return render(request, 'login.html', data)
            
    return render(request,'dashboard.html')