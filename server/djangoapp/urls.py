from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView


app_name = 'djangoapp'

urlpatterns = [
    # path for login API
    path(route='login', view=views.login_user, name='login'),

    # path for login page (React)
    path('login/', TemplateView.as_view(template_name="index.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)