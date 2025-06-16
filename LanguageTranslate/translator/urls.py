from django.urls import path
from .views import home_view,translate_text,extract_text, dashboard

urlpatterns = [
    path("", home_view, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("upload/", extract_text, name="upload_image"),
    path("translate/", translate_text, name="translate_text"),
]


