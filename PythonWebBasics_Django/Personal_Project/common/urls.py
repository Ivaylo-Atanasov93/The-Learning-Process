from django.urls import path

from common.views import landing_page, lesson_booking

urlpatterns = [
    path('', landing_page, name='index'),
    path('booking/', lesson_booking, name='booking')
]
