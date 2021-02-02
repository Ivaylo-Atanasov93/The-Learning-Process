from django.urls import path
from pets.views import pets_list, show_pet_details, like_pet

urlpatterns = [
    path('', pets_list, name='list pets'),
    path('details/<int:pk>/', show_pet_details, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),
]
