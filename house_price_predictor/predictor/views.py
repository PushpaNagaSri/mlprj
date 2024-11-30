# house_price_predictor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import HousePriceForm
import joblib

# Home page view with house price prediction form
def home(request):
    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            # Load the model
            model = joblib.load('house_price_model.pkl')

            # Extract form data
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft = form.cleaned_data['sqft']

            # Make prediction
            prediction = model.predict([[bedrooms, bathrooms, sqft]])[0]

            return render(request, 'result.html', {'prediction': prediction})
    else:
        form = HousePriceForm()

    return render(request, 'home.html', {'form': form})

# Register page view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login page view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')
