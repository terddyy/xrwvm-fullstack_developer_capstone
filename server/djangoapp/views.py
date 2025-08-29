from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Example API view
def get_cars(request):
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Corolla"},
        {"id": 2, "brand": "Honda", "model": "Civic"},
        {"id": 3, "brand": "Ford", "model": "Focus"},
    ]
    return JsonResponse(cars, safe=False)

# Login function
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return JsonResponse({"error": "Invalid credentials"})
    return JsonResponse({"message": "Send a POST request with username and password"})

# Logout function
def logout_user(request):
    logout(request)
    return redirect("/")
