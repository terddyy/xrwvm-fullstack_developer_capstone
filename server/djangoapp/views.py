import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .restapis import get_request, analyze_review_sentiments, post_review


# Example API view
def get_cars(request):
    cars = [
        {"id": 1, "brand": "Toyota", "model": "Corolla"},
        {"id": 2, "brand": "Honda", "model": "Civic"},
        {"id": 3, "brand": "Ford", "model": "Focus"},
    ]
    return JsonResponse(cars, safe=False)


# Login function
# @csrf_exempt
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return JsonResponse({"status": 200, "message": "Login successful"})
#         else:
#             return JsonResponse({"status": 401, "message": "Invalid credentials"})
#     return JsonResponse({"status": 405, "message": "Method not allowed"})
    
# @csrf_exempt
# def login_user(request):
#     if request.method == "POST":
#         try:
#             if request.content_type == "application/json":
#                 data = json.loads(request.body.decode("utf-8"))
#                 username = data.get("username")
#                 password = data.get("password")
#             else:
#                 username = request.POST.get("username")
#                 password = request.POST.get("password")

#             if not username or not password:
#                 return JsonResponse({"status": 400, "message": "Missing credentials"})

#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return JsonResponse({"status": 200, "message": "Login successful"})
#             else:
#                 return JsonResponse({"status": 401, "message": "Invalid credentials"})

#         except Exception as e:
#             return JsonResponse({"status": 500, "message": f"Server error: {str(e)}"})
#     return JsonResponse({"status": 405, "message": "Method not allowed"})

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            if request.content_type == "application/json":
                data = json.loads(request.body.decode("utf-8"))
                username = data.get("username")
                password = data.get("password")
            else:
                username = request.POST.get("username")
                password = request.POST.get("password")

            if not username or not password:
                return JsonResponse({"status": 400, "message": "Missing credentials"})

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({"status": 200, "message": "Login successful"})
            else:
                return JsonResponse({"status": 401, "message": "Invalid credentials"})
        except Exception as e:
            return JsonResponse({"status": 500, "message": str(e)})
    return JsonResponse({"status": 405, "message": "Method not allowed"})


# Logout function
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"status": 200, "message": "Logged out"})


# Get Dealerships
def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


# Get Dealer Details
def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    return JsonResponse({"status": 400, "message": "Bad Request"})


# Get Dealer Reviews with Sentiment
def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            review_detail['sentiment'] = response.get('sentiment', 'unknown')
        return JsonResponse({"status": 200, "reviews": reviews})
    return JsonResponse({"status": 400, "message": "Bad Request"})


# Add Review function
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"status": 403, "message": "Unauthorized"})

        try:
            data = json.loads(request.body.decode("utf-8"))
            response = post_review(data)  # Call helper in restapis.py
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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            # Parse JSON body
            data = json.loads(request.body)

            userName = data.get("userName")
            password = data.get("password")
            firstName = data.get("firstName")
            lastName = data.get("lastName")
            email = data.get("email")

            # Validation (basic)
            if not userName or not password:
                return JsonResponse({"error": "Username and password are required"}, status=400)

            if User.objects.filter(username=userName).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists"}, status=400)

            # Create user
            user = User.objects.create_user(
                username=userName,
                password=password,
                first_name=firstName,
                last_name=lastName,
                email=email
            )

            return JsonResponse({
                "status": True,
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Method Not Allowed"}, status=405)

