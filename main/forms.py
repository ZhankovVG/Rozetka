from django import forms
from .models import *
from .models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['accept'] = 'user_images/'
