from django import forms

from app.models import *
from django.core import validators

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = '__all__'
        widgets = {'password':forms.PasswordInput}
        validators = {'mobile':validators.RegexValidator('[6-9]\d{9}')}