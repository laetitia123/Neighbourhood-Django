from django import forms

from .models import *


class uploadimageForm(forms.Form):
    class Meta:
         model=Neighbour
         exclude=('user',)

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('Name', 'profile_picture', 'bio')
        # exclude=['user']





class CommentForm(forms.ModelForm):
  
    class Meta:
        model = Comment
        fields = ('comment',)

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

