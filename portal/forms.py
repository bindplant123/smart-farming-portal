from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Crop
import re


# ==========================================================
# 🔐 SMART LOGIN FORM (Email OR 10-digit Mobile + Password)
# ==========================================================
class SmartLoginForm(forms.Form):

    email_or_phone = forms.CharField(
        max_length=100,
        label="Email or Mobile Number",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter email or 10-digit mobile",
            "autocomplete": "username"
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password",
            "autocomplete": "current-password"
        })
    )

    def clean_email_or_phone(self):
        value = self.cleaned_data.get("email_or_phone", "").strip()

        # If digits → validate mobile
        if value.isdigit():
            if len(value) != 10:
                raise ValidationError("Mobile number must be exactly 10 digits.")
        else:
            # Validate as email
            from django.core.validators import validate_email
            try:
                validate_email(value)
            except ValidationError:
                raise ValidationError("Enter a valid email address.")

        return value


# ==========================================================
# 📝 USER REGISTRATION FORM
# ==========================================================
class UserRegistrationForm(forms.Form):

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter username"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter email"
        })
    )

    mobile = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Enter a valid 10-digit mobile number."
            )
        ],
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter 10-digit mobile number"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password"
        })
    )

    # ✅ Field-level validation
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already registered.")

        return email

    # ✅ Full form validation
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Passwords do not match.")

            # Use Django's built-in password validation
            try:
                validate_password(password)
            except ValidationError as e:
                raise ValidationError(e.messages)

        return cleaned_data


# ==========================================================
# 🌱 SMART CROP CALENDAR FORM
# ==========================================================
class CropCalendarForm(forms.Form):

    crop = forms.ModelChoiceField(
        queryset=Crop.objects.all(),
        empty_label="Select Crop",
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    sowing_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )