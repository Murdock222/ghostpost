from django import forms
from homepage.models import BoastsAndRoasts

TRUE_FALSE_CHOICES = (
    (True, 'roast'),
    (False, 'boast')
)

class CreatePost(forms.ModelForm):
    class Meta:
        model = BoastsAndRoasts
        fields = ["isroast", "post_content"]
        widgets = {'isroast': forms.Select(choices=TRUE_FALSE_CHOICES)}