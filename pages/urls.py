from django.urls import path
from .views import HomeView, ImpressumView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('impressum/', ImpressumView.as_view(), name='impressum'),
]