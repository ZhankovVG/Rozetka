from django import forms
from .models import Review, RatingsStar, Rating


class ReviewForm(forms.ModelForm):
    # Adding a comment
    class Meta:
        model = Review
        fields = (
            'name', 'text', 'email'
        )


class RatingForm(forms.ModelForm):
    # Add rating form
    star = forms.ModelChoiceField(
        queryset=RatingsStar.objects.all(), widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)