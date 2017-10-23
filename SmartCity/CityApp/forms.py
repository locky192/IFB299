from django import forms
from django.contrib.auth.models import User
from CityApp.models import UserProfile

class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'unit_number', 'street_number', 'street_name',
                  'suburb', 'state', 'postcode', 'user_type')


class UpdateProfile(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


    def save(self, commit=True):
        user = super(UpdateProfile, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UpdateUserProfile(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'unit_number', 'street_number', 'street_name',
                          'suburb', 'state', 'postcode', 'user_type')

    def save(self, commit=True):
        user = super(UpdateUserProfile, self).save(commit=False)

        if commit:
            user.save()

        return user
