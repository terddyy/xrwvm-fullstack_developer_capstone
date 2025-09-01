from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path("api/add_review/", views.add_review, name="add_review"),

    # Default index page
    path('', TemplateView.as_view(template_name="index.html")),

    # Path for dealerships
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # Path for dealer details
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # Path for dealer reviews
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
]
