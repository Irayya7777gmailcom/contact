from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'country', 'zip_code']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Add custom validation logic for phone_number if needed
        return phone_number

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        # Add custom validation logic for zip_code if needed
        return zip_code

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom validation logic for email if needed
        return email

    # Simplified versions of fields with custom validation
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(label='Phone Number', max_length=15, required=False)
    address = forms.CharField(label='Address', widget=forms.Textarea, required=False)
    city = forms.CharField(label='City', max_length=50, required=False)
    state = forms.CharField(label='State', max_length=50, required=False)
    country = forms.CharField(label='Country', max_length=50, required=False)
    zip_code = forms.CharField(label='ZIP Code', max_length=10, required=False)
