from django import forms
from django.core.validators import ValidationError


class TodoForm(forms.Form):

    title = forms.CharField(
        min_length=5,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form_control',
            }
        ),
        required=True,
    )
    description = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
            }
        ),
        required=True,
    )

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise ValidationError('This is a bot!')


def min_validator_title(value):
    if not value or len(value) < 5:
        raise ValidationError(f'Value should be at least 5 symbols, it`s {len(value)} instead!')


def min_validator_description(value):
    if not value or len(value) < 10:
        raise ValidationError(f'Value should be at least 10 symbols, it`s {len(value)} instead!')


def max_validator_title(value):
    if len(value) > 30:
        raise ValidationError(f'Value should be maximum 30 symbols, it`s {len(value)} instead')


def max_validator_description(value):
    if len(value) > 100:
        raise ValidationError(f'Value should be maximum 100 symbols, it`s {len(value)} instead')

    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form_control',
    #         }
    #     ),
    # )
    # priority = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     )
    # )
    # size = forms.IntegerField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'type': 'range',
    #             'class': 'form-control',
    #         },
    #     )
    # )
