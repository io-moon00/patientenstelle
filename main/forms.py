from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactForm(forms.Form):
    required_css_class = 'required'
    SALUTATION = [
        ('mr', 'Herr'),
        ('mrs', 'Frau'),
        ('other', 'Andere'),
    ]
    salutation = forms.CharField(label='Anrede', max_length=4, widget=forms.Select(choices=SALUTATION,
                                                                                   attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-main focus:border-main block p-2'}))
    prename = forms.CharField(max_length=100, 
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Vorname'}))
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Nachname'}))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-main focus:border-main block w-full p-2.5',
                                                     'placeholder': 'E-Mail'}))
    phone = forms.CharField(label='Telefonnummer', max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Telefon'}))
    message = forms.CharField(label='Nachricht', required=True,
                            widget=forms.Textarea(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main'}))
    data_policy_accepted = forms.BooleanField(required=True,
                                              widget=forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-main dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2',
                                                     'placeholder': 'Telefon'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        'inv': 'reCaptcha-Validierung fehlgeschlagen. Bitte versuche es später noch einmal oder kontaktiere mich via info@cams-world.de, wenn das Problem weiterhin besteht.'
    })

class MembershipForm(forms.Form):
    required_css_class = 'required'
    SALUTATION = [
        ('mr', 'Herr'),
        ('mrs', 'Frau'),
        ('other', 'Andere'),
    ]
    salutation = forms.CharField(label='Anrede', max_length=4, widget=forms.Select(choices=SALUTATION,
                                                                                   attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-main focus:border-main block p-2'}))
    prename = forms.CharField(max_length=100, 
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Vorname'}))
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Nachname'}))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-main focus:border-main block w-full p-2.5',
                                                     'placeholder': 'E-Mail'}))
    phone = forms.CharField(label='Telefonnummer', max_length=20, required=False,
                            widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Telefon'}))
    street = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Strasse und Hausnummer'}))
    plz = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': '0000'}))
    place = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main',
                                                     'placeholder': 'Ort'}))
    message = forms.CharField(label='Nachricht', required=False,
                            widget=forms.Textarea(attrs={'class': 'block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg shadow-sm bg-gray-50 focus:ring-main focus:border-main'}))
    data_policy_accepted = forms.BooleanField(required=True,
                                              widget=forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-primary-600 bg-gray-100 border-gray-300 rounded focus:ring-main dark:focus:ring-primary-600 dark:ring-offset-gray-800 focus:ring-2',
                                                     'placeholder': 'Telefon'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        'inv': 'reCaptcha-Validierung fehlgeschlagen. Bitte versuche es später noch einmal oder kontaktiere mich via info@cams-world.de, wenn das Problem weiterhin besteht.'
   })
