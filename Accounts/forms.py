from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, \
    PasswordResetForm, UsernameField
from django.utils.translation import gettext_lazy as _
from Accounts.models import User,Profile


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'}),
    )
    extra_kwargs = {"password1": {'write_only': True}}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'bty'),
                'style': (
                    'width:98%;')
            })

    class Meta:
        model = User
        fields = ('username','email','mobile_number',)

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'PhoneNumber'
            }),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Password'
    }))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Old Password'
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        
            
            'first_name',
            'last_name',
            'username',
            'email',
            
            'mobile_number',
            'national_id',

            
            'next_of_kin',
            'member_code',
        
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'form-group '),
                'placeholder': field,
                'style': (
                    'width:98%;'
                    'border-radius: 8px;'
                    'resize: none;'
                    'color:  # 001100;'
                    'height: 40px;'
                    'border: 1px solid  # 4141;'
                    'background-color: transparent;'
                    ' font-family: inherit;'

                ),

            })

class User_ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
        
            'registration_number',
            'about',
            'gender',
            'blood_group',
            'country',
            'county',
            'state',
            'postal_code',
            'town_near',
            'allergies',
            'medical_conditions',
            'price_per_consultation',

        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'form-group '),
                'placeholder': field,
                'style': (
                    'width:98%;'
                    'border-radius: 8px;'
                    'resize: none;'
                    'color:  # 001100;'
                    'height: 40px;'
                    'border: 1px solid  # 4141;'
                    'background-color: transparent;'
                    ' font-family: inherit;'

                ),

            })


    # medical_conditions = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             "rows": 3,
    #             "placeholder": "List any chronic conditions, surgeries, etc.",
    #         }
    #     ),
    # )
    # allergies = forms.CharField(
    #     required=False,
    #     widget=forms.Textarea(
    #         attrs={
    #             "rows": 3,
    #             "placeholder": "List any allergies to medications, food, etc.",
    #         }
    #     ),
    # )
    