"""
Definition of forms.
"""


from email.policy import default
from django.forms import RadioSelect, forms
from random import choices
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class AnketaForm (forms.Form):
    
    name = forms.CharField(label= 'Name', min_length=2, max_length=100)
    
    city = forms.CharField(label='City', min_length=2, max_length=100)
    job = forms.CharField(label='Job ', min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Yo gender', choices=[('1','Man'), ('2','Woman')],
                               widget=forms.RadioSelect, initial=1)
    internet =forms.ChoiceField(label='Do you use the Internet',
                                choices=(('1', 'Every day'),
                                        ('2', 'several times a day'),
                                         ('3', 'several times a week'),
                                         ('4', 'several times a month')), initial=1)
    notice = forms.BooleanField(label='Receive news by e-mail?',
                                required=False)
    email = forms.EmailField(label='You e-mail', min_length=7)
    message = forms.CharField(label='Briefly about yourself', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
    

   
     
        