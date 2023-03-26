from django.forms import ModelForm
from .models import Postmodel


class PostForm(ModelForm):
    class Meta:
        model = Postmodel
        fields = ['title', 'content', 'category']
