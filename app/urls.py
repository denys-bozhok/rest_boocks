from django.urls import path
from .views import Home


urlpatterns = [
    path('', Home.as_view()),
    path('<int:arg>', Home.as_view()),
]