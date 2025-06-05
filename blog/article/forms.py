from django import forms
from . import models

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Article

        fields = [
            'title',
            'text'
        ]

        # labels = {
        #   'user': 'Пользователь',
        #   'title': 'Заголовок',
        #   'text': 'Содержимое',  
        # }

        # widgets = {
        #     'dt': forms.DateInput(attrs={'type': 'datetime-local'}),
        #     'color': forms.TextInput(attrs={'type':'color'}),
        # }