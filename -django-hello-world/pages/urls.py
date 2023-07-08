#new
from django.urls import URLPattern, path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
]