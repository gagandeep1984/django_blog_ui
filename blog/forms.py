from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=300,
        min_length=50,
        required=True,
        label="Title",
        label_suffix=": ",
    )

    class Meta:
        model = Blog
        fields = "__all__"
        exclude = ["likes", "created_at", "updated_at"]
