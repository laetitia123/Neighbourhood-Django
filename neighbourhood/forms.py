from django import forms

from .models import *


class uploadimageForm(forms.Form):
    class Meta:
         model=Neighbour
         exclude=('user',)

class ProfileForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ('first_name', 'location', 'last_name',)
        # exclude=['user']


class AddBusinessForm(forms.ModelForm):
    # own= models.CharField(max_length =30)
    # name= models.CharField(max_length =30)
    # email= models.CharField(max_length =30)
    # description = models.CharField(max_length =30)
    # date_post= models.DateTimeField(max_length =20)
    # location = models.CharField(max_length =60)
    

    class Meta:
        model = Business
        fields = ('owner', 'name', 'email','description','date_post','location')
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

