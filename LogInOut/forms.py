from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    class Meta:
        model = User
        fields = ('username','email')
        widgets = {'username':forms.TextInput(
            attrs={'class':'form-control'}
        )}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus':True,
        'class':'form-control',}
    ))
    password = forms.CharField(
        label = "Password",
        strip = False,
        widget = forms.PasswordInput(
            attrs={'autocomplete':'current-password',
            'class':'form-control'}
        ),
    )


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label = "Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
        'autofocus':True, 'class':'form-control'}),
    )

    new_password1 = forms.CharField(
        label = "New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
        'class':'form-control'}),
    )

    new_password2 = forms.CharField(
        label = "Confirm New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
        'class':'form-control'}),
    )


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email',
        'class':'form-control'})
    )


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "Confirm New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )