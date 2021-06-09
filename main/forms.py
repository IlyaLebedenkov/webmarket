from django import forms
from .models import Comment
from django.contrib.auth.models import User



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'username', 'text', 'product', 'img'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]