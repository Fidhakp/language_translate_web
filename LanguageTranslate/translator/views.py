# # from django.shortcuts import render, redirect
# # from django.contrib.auth import login, logout
# # from django.contrib.auth.decorators import login_required
# # from .forms import RegisterForm, LoginForm, TranslationForm
# # from googletrans import Translator


# # # Homepage (Landing Page)
# # def home_view(request):
# #     return render(request, "translator/home.html")  #  Loads homepage

# # #  User Registration
# # def register_view(request):
# #     if request.method == "POST":
# #         form = RegisterForm(request.POST)
# #         if form.is_valid():
# #             user = form.save(commit=False)
# #             user.set_password(form.cleaned_data["password"])  # Hash password
# #             user.save()
# #             login(request, user)  # Auto-login after registration
# #             return redirect("translate")  # Redirect to translation page
# #     else:
# #         form = RegisterForm()
# #     return render(request, "translator/register.html", {"form": form})

# # #  User Login
# # def login_view(request):
# #     if request.method == "POST":
# #         form = LoginForm(data=request.POST)
# #         if form.is_valid():
# #             user = form.get_user()
# #             login(request, user)
# #             return redirect("dashboard")  #  Redirects to dashboard
# #         else:
# #             return render(request, "translator/login.html", {"form": form, "error": "Invalid credentials"})
# #     else:
# #         form = LoginForm()
# #     return render(request, "translator/login.html", {"form": form})


# # @login_required
# # def dashboard(request):
# #     return render(request, "translator/dashboard.html")

# # # User Logout
# # def logout_view(request):
# #     logout(request)
# #     return redirect("login")  # Redirects to login after logout
# # from django.contrib.auth.decorators import login_required

# # # Translation Function (Requires Login)
# # @login_required
# # def translate_text(request):
# #     translated_text = None
# #     if request.method == "POST":
# #         form = TranslationForm(request.POST)
# #         if form.is_valid():
# #             text = form.cleaned_data["text"]
# #             target_language = form.cleaned_data["language"]
# #             translator = Translator()
# #             translated_text = translator.translate(text, dest=target_language).text
# #     else:
# #         form = TranslationForm()
# #     return render(request, "translator/translate.html", {"form": form, "translated_text": translated_text})

# # import pytesseract
# # from PIL import Image
# # from django.core.files.storage import FileSystemStorage
# # from django.contrib.auth.decorators import login_required
# # from googletrans import Translator
# # from .forms import TranslationForm, ImageUploadForm
# # from .models import UploadedImage

# # pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

# # # Load an image (replace "test_image.png" with your own file)
# # image = Image.open("test_image.png")
# # extracted_text = pytesseract.image_to_string(image)

# # print("Extracted Text:", extracted_text)

# # @login_required
# # def translate_text(request):
# #     translated_text = None
# #     extracted_text = None

# #     if request.method == "POST":
# #         form = TranslationForm(request.POST)
# #         image_form = ImageUploadForm(request.POST, request.FILES)

# #         if form.is_valid() or image_form.is_valid():
# #             text = form.cleaned_data.get("text", "")
# #             target_language = form.cleaned_data["language"]
# #             image = image_form.cleaned_data.get("image")

# #             # OCR Processing
# #             if image:
# #                 fs = FileSystemStorage()
# #                 filename = fs.save(image.name, image)
# #                 image_path = fs.path(filename)
# #                 extracted_text = pytesseract.image_to_string(Image.open(image_path))
# #                 text = extracted_text if extracted_text.strip() else text

# #             # Translation
# #             if text:
# #                 translator = Translator()
# #                 translated_text = translator.translate(text, dest=target_language).text

# #     else:
# #         form = TranslationForm()
# #         image_form = ImageUploadForm()

# #     return render(
# #         request, 
# #         "translator/translate.html", 
# #         {
# #             "form": form, 
# #             "image_form": image_form, 
# #             "translated_text": translated_text, 
# #             "extracted_text": extracted_text
# #         }
# #     )

# import os
# import pytesseract
# from PIL import Image
# from django.shortcuts import render, redirect
# from django.core.files.storage import FileSystemStorage
# from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required
# from googletrans import Translator
# from .forms import RegisterForm, LoginForm, TranslationForm, ImageUploadForm
# from .models import UploadedImage  # Ensure this model exists

# # Set the path to Tesseract
# pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

# # Homepage (Landing Page)
# def home_view(request):
#     return render(request, "translator/home.html")

# # User Registration
# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password"])
#             user.save()
#             login(request, user)
#             return redirect("translate")  # Redirect to translation page
#     else:
#         form = RegisterForm()
#     return render(request, "translator/register.html", {"form": form})

# # User Login
# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("dashboard")  # Redirect to dashboard
#         else:
#             return render(request, "translator/login.html", {"form": form, "error": "Invalid credentials"})
#     else:
#         form = LoginForm()
#     return render(request, "translator/login.html", {"form": form})

# # Dashboard (Requires Login)
# @login_required
# def dashboard(request):
#     return render(request, "translator/dashboard.html")

# # User Logout
# def logout_view(request):
#     logout(request)
#     return redirect("login")

# # Translation Function (Text & Image Processing)
# @login_required
# def translate_text(request):
#     translated_text = None
#     extracted_text = None

#     if request.method == "POST":
#         form = TranslationForm(request.POST, request.FILES)

#         if form.is_valid():
#             text = form.cleaned_data.get("text", "")
#             target_language = form.cleaned_data["language"]
           

import os
import pytesseract
from PIL import Image
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from googletrans import Translator
from .forms import RegisterForm, LoginForm, TranslationForm
from .models import UploadedImage  # Ensure this model exists

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

# Homepage (Landing Page)
def home_view(request):
    return render(request, "translator/home.html")

# User Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("translate")
    else:
        form = RegisterForm()
    return render(request, "translator/register.html", {"form": form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")  # ✅ Ensure dashboard is correctly mapped in URLs
        else:
            return render(request, "translator/login.html", {"form": form, "error": "Invalid credentials"})
    else:
        form = LoginForm()
    return render(request, "translator/login.html", {"form": form})

# Dashboard (Requires Login)
@login_required
def dashboard(request):
    return render(request, "translator/dashboard.html")

# User Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

# Translation Function (Text & Image Processing)
@login_required
def translate_text(request):
    translated_text = None
    extracted_text = None

    if request.method == "POST":
        form = TranslationForm(request.POST, request.FILES)

        if form.is_valid():
            text = form.cleaned_data.get("text", "")
            target_language = form.cleaned_data["language"]
            image = request.FILES.get("image")

            # OCR Processing
            if image:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_path = fs.path(filename)

                if os.path.exists(image_path):  # Ensure image exists before processing
                    extracted_text = pytesseract.image_to_string(Image.open(image_path))
                    text = extracted_text if extracted_text.strip() else text
                else:
                    extracted_text = "Error: Image file not found."

            # Translation
            if text.strip():
                translator = Translator()
                translated_text = translator.translate(text, dest=target_language).text

    else:
        form = TranslationForm()

    return render(
        request,
        "translator/translate.html",
        {
            "form": form,
            "translated_text": translated_text,
            "extracted_text": extracted_text,
        }
    )

import os
import pytesseract
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

@login_required
def extract_text(request):
    extracted_text = None

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            image = request.FILES.get("image")  # Get uploaded image

            if image:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_path = fs.path(filename)

                if os.path.exists(image_path):
                    extracted_text = pytesseract.image_to_string(Image.open(image_path))
                else:
                    extracted_text = "Error: Image file not found."

    else:
        form = ImageUploadForm()

    return render(
        request,
        "translator/extract_text.html",
        {"form": form, "extracted_text": extracted_text}
    )


from .forms import TranslationForm  # Make sure this is imported

@login_required
def extract_text(request):
    extracted_text = None

    if request.method == "POST":
        form = TranslationForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data.get("image")
            target_language = form.cleaned_data.get("language")

            if image:
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_path = fs.path(filename)

                if os.path.exists(image_path):
                    extracted_text = pytesseract.image_to_string(Image.open(image_path))
                    # You can optionally process translated text here too

    else:
        form = TranslationForm()

    return render(request, "translator/extract_text.html", {
        "form": form,
        "extracted_text": extracted_text,
    })