from django.urls import path
from .views import BoshSahifaView
urlpatterns = [
    path('', BoshSahifaView.as_view(), name="bosh")
]