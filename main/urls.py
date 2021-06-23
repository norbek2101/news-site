from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('davlatlar/', davlatlar, name="davlatlar"),
    path('create/', create, name="country_create"),
    path('delete/<int:id>', delete, name="country_delete"),
    path('update/<int:id>', update, name="country_update"),
    path('create2/', CreateView.as_view(), name='create_view'),

]
