from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('get_cars/', views.get_cars, name='get_cars'),
    

    # Default index page
    path('', TemplateView.as_view(template_name="index.html")),


    #path for get dealerships
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),

    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
]
