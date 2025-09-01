from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# React entry point
index_view = never_cache(TemplateView.as_view(template_name="index.html"))

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    path("djangoapp/", include("djangoapp.urls")),

    # Django app routes (API/backend)
    path('djangoapp/', include('djangoapp.urls')),

    # Django-rendered pages
    path('', TemplateView.as_view(template_name="Home.html"), name="home"),
    path('about/', TemplateView.as_view(template_name="About.html"), name="about"),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name="contact"),

    # React-rendered pages
    path('login/', index_view, name="login"),
    path('dealers/', index_view, name="dealers"),

    # Catch-all for other React routes (optional)
    re_path(r'^.*$', index_view),
]

# Serve static & media in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
