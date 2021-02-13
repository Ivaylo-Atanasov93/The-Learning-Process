from django import forms
from django.core import validators


class BookingForm(forms.Form):
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )

    TIMEFRAME_CHOICES = (
        ('9:00 to 10:00', '9:00 to 10:00'),
        ('10:00 to 11:00', '10:00 to 11:00'),
        ('11:00 to 12:00', '11:00 to 12:00'),
        ('12:00 to 13:00', '12:00 to 13:00'),
        ('13:00 to 14:00', '13:00 to 14:00'),
        ('14.00 to 15:00', '14.00 to 15:00'),
        ('15:00 to 16:00', '15:00 to 16:00'),
        ('16:00 to 17:00', '16:00 to 17:00'),
        ('17:00 to 18:00', '17:00 to 18:00'),
        ('18:00 to 19:00', '18:00 to 19:00'),
    )
    name = forms.CharField(max_length=20, required=True)
    surname = forms.CharField(max_length=20, required=True)
    phone = forms.CharField(
        max_length=11,
    )
    email = forms.EmailField(
        required=True,
        validators=[validators.EmailValidator]
    )
    day = forms.CharField(
        label='Which day?',
        widget=forms.Select(choices=DAY_CHOICES),
        required=True,
    )
    time = forms.CharField(
        label='At what time?',
        widget=forms.Select(choices=TIMEFRAME_CHOICES),
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )
