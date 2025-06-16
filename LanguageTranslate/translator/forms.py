# # from django import forms
# # from django.contrib.auth.models import User
# # from django.contrib.auth.forms import AuthenticationForm
# # from .models import UploadedImage  #  Import model for image uploads

# # # 🔹 Text Translation Form
# # class TranslationForm(forms.Form):
# #     text = forms.CharField(widget=forms.Textarea, label="Enter text to translate")
# #     language = forms.ChoiceField(
# #         choices=[
# #             ("en", "English"),
# #             ("es", "Spanish"),
# #             ("fr", "French"),
# #             ("de", "German"),
# #             ("hi", "Hindi"),
# #         ],
# #         label="Select Language",
# #     )

# # # 🔹 User Registration Form
# # class RegisterForm(forms.ModelForm):
# #     password = forms.CharField(widget=forms.PasswordInput)
    
# #     class Meta:
# #         model = User
# #         fields = ["username", "email", "password"]

# # # 🔹 User Login Form
# # class LoginForm(AuthenticationForm):
# #     username = forms.CharField(label="Username")
# #     password = forms.CharField(widget=forms.PasswordInput, label="Password")

# # # 🔹 Image Upload Form (NEW)
# # class ImageUploadForm(forms.ModelForm):
# #     class Meta:
# #         model = UploadedImage  #  Connects to our UploadedImage model
# #         fields = ["image"]
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from .models import UploadedImage  # Ensure this model exists

# # 🔹 Translation Form (Text & Image Processing)
# class TranslationForm(forms.Form):
#     text = forms.CharField(
#         widget=forms.Textarea, 
#         label="Enter text to translate", 
#         required=False
#     )
#     image = forms.ImageField(
#         label="Upload Image (optional)", 
#         required=False
#     )
#     language = forms.ChoiceField(
#         choices=[
#             ("en", "English"),
#             ("es", "Spanish"),
#             ("fr", "French"),
#             ("de", "German"),
#             ("hi", "Hindi"),
#         ],
#         label="Select Language"
#     )

# # 🔹 Image Upload Form (Now using ModelForm for better handling)
# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = UploadedImage  # Ensure this model exists in models.py
#         fields = ["image"]

# # 🔹 User Registration Form
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ["username", "email", "password"]

# # 🔹 User Login Form
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Username")
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UploadedImage  # Ensure this model exists

# 🔹 Available Languages (Easier to Update)
LANGUAGE_CHOICES = [
    ("en", "English"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("de", "German"),
    ("hi", "Hindi"),
        ("ml", "Malayalam"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("kn", "Kannada"),
    ("gu", "Gujarati"),
    ("mr", "Marathi"),
    ("pa", "Punjabi"),
    ("bn", "Bengali"),
    ("ur", "Urdu"),
    ("ar", "Arabic"),
    ("zh", "Chinese"),
    ("ja", "Japanese"),
    ("ko", "Korean"),
    ("ru", "Russian"),
    ("it", "Italian"),
    ("pt", "Portuguese"),

]

# 🔹 Translation Form (Text & Image Processing)
class TranslationForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter text to translate"}), 
        label="Text for Translation", 
        required=False
    )
    image = forms.ImageField(
        label="Upload Image (optional)", 
        required=False
    )
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        label="Select Language"
    )

    # ✅ Ensure at least text or image is provided
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text", "").strip()
        image = cleaned_data.get("image")

        if not text and not image:
            raise forms.ValidationError("Please provide either text or an image for translation.")

        return cleaned_data

# 🔹 Image Upload Form (Using ModelForm for Better Handling)
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ["image"]

# 🔹 User Registration Form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

# 🔹 User Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"placeholder": "Enter username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}))