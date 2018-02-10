from django import forms
from django.contrib.auth.forms import UserCreationForm
from website.apps.item.models import Donation

class DonationForm(UserCreationForm):

    name = forms.CharField(max_length=30, required=True, help_text='General Name of Item')
    text_description = forms.CharField(max_length=500, required=True, help_text='Describe the Item')
    img_link = forms.URLField(max_length=200, required=True, help_text='Link to Images of Item (use a different site)')
    city = forms.CharField(max_length=30, required=True, help_text='In what city is the Item')
    donor_email = forms.EmailField(max_length=255, required=True, help_text='How can we get in contact')

    # Be sure to add extra fields here
    class Meta:
        model = Donation
        fields = (  'name',
                    'text_description',
                    'img_link',
                    'city',
                    'donor_email',
                    )