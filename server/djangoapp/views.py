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


def get_dealerships(request, state="All"):
    if(state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/"+state
    dealerships = get_request(endpoint)
    return JsonResponse({"status":200,"dealers":dealerships})


def get_dealer_details(request, dealer_id):
    if(dealer_id):
        endpoint = "/fetchDealer/"+str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status":200,"dealer":dealership})
    else:
        return JsonResponse({"status":400,"message":"Bad Request"})


def get_dealer_reviews(request, dealer_id):
    # if dealer id has been provided
    if(dealer_id):
        endpoint = "/fetchReviews/dealer/"+str(dealer_id)
        reviews = get_request(endpoint)
        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            print(response)
            review_detail['sentiment'] = response['sentiment']
        return JsonResponse({"status":200,"reviews":reviews})
    else:
        return JsonResponse({"status":400,"message":"Bad Request"})
