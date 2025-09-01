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
]
