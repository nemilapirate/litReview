from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.CreateReviewModel
        fields = ['title', 'description', 'image', 'rating', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )
        self.fields['rating'].widget = forms.RadioSelect(choices=choices)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'body', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )
        self.fields['rating'].widget = forms.RadioSelect(choices=choices)


class ReviewFormDelete(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
