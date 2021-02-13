from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.
from common.forms import BookingForm
from common.models import Booking


def landing_page(request):
    form = BookingForm
    context = {
        'lesson_booking': form,
    }
    return render(request, 'index.html', context)


@require_POST
def lesson_booking(request):
    form = BookingForm(request.POST)
    if form.is_valid():

        name = form.cleaned_data['name']
        surname = form.cleaned_data['surname']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        day = form.cleaned_data['day']
        time = form.cleaned_data['time']
        message = form.cleaned_data['message']

        booked_lesson = Booking(
            name=name,
            surname=surname,
            phone=phone,
            email=email,
            day=day,
            time=time,
            message=message
        )
        booked_lesson.save()
        context = {
            'booking': booked_lesson,
        }
        message = ''
        message += f'Name: {name}\n'
        message += f'Surname: {surname}\n'
        message += f'Phone: {phone}\n'
        message += f'E-mail: {email}\n'
        message += f'Day: {day}\n'
        message += f'Time: {time}\n'
        message += f'Message: {message}\n'

        # send_mail(
        #     'New lesson booked',
        #     f'{message}',
        #     '',
        #     ['ivailo.atanasov93@gmail.com'],
        #     fail_silently=False,
        # )
        return render(request, 'created_booking.html', context)
    return render(request, 'contact.html')
