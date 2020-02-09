from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'image',
                  'draft',
                  'publish',
                  ]
