from django import forms


# class TodoForm(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'neshto-si'
#             }
#         )
#     )
#     description = forms.CharField()
#
#     def __init__(self):
#         super().__init__()
#         for (field_name, field) in self.fields.items():
#             if 'class' in field.widget.attrs:
#                 value = field.widget.attrs['class'] + ' form-control'
#             else:
#                 value = 'form-control'
#             field.widget.attrs['class'] = value

class TodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form_control',
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
            }
        ),
        required=False,
    )
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
