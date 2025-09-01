# restapis.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv("sentiment_analyzer_url", default="http://localhost:5050")


def get_request(endpoint, **kwargs):
    """
    Perform a GET request to backend_url + endpoint
    """
    try:
        response = requests.get(backend_url + endpoint, params=kwargs)
        response.raise_for_status()
        print(f"GET from {response.url}")  # Debug log
        return response.json()
    except Exception as e:
        print(f"Error in get_request: {e}")
        return {"error": str(e)}


def analyze_review_sentiments(text):
    """
    Call sentiment analyzer microservice
    """
    try:
        request_url = sentiment_analyzer_url + "analyze/" + text
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error in analyze_review_sentiments: {e}")
        return {"sentiment": "unknown", "error": str(e)}


def post_review(data_dict):
    """
    Post review data to backend
    """
    try:
        request_url = backend_url + "/insert_review"  # keep consistent with your earlier backend
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())  # Debug log
        return response.json()
    except Exception as e:
        print(f"Error in post_review: {e}")
        return {"status": "error", "message": str(e)}
