import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# If you have a helper to send reviews (adjust the import to your actual location)
# from .utils import post_review

# Example API view
def get_cars(request):
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Corolla"},
        {"id": 2, "brand": "Honda", "model": "Civic"},
        {"id": 3, "brand": "Ford", "model": "Focus"},
    ]
    return JsonResponse(cars, safe=False)


# Login function
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"status": 200, "message": "Login successful"})
        else:
            return JsonResponse({"status": 401, "message": "Invalid credentials"})
    return JsonResponse({"status": 405, "message": "Method not allowed"})


# Logout function
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"status": 200, "message": "Logged out"})


# Add Review function
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"status": 403, "message": "Unauthorized"})

        try:
            data = json.loads(request.body.decode("utf-8"))

            # This is where you integrate with your review posting logic
            # Example: response = post_review(data)
            # For now, we’ll simulate success:
            response = {"review": data, "status": "saved"}

            return JsonResponse({
                "status": 200,
                "message": "Review posted successfully",
                "response": response
            })

        except Exception as e:
            return JsonResponse({
                "status": 400,
                "message": f"Error in posting review: {str(e)}"
            })

    return JsonResponse({"status": 405, "message": "Method not allowed"})
