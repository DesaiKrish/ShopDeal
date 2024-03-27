from django import forms
from .models import User

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)
    address = forms.CharField(max_length=100)
    phone_num = forms.CharField(max_length=20)
    role = forms.ChoiceField(choices=[('customer', 'Customer'), ('seller', 'Seller')])

    def save(self):
        # Create a new user object
        user = User.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            address=self.cleaned_data['address'],
            phone_num=self.cleaned_data['phone_num']
        )
        # You may handle the role here separately or associate it with user in any other way as needed
        return user
