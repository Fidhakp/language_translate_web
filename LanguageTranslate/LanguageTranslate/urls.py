from django.urls import path, include
from translator.views import home_view, register_view, login_view, logout_view, translate_text, dashboard  # ✅ Import dashboard

urlpatterns = [
    path("", home_view, name="home"),  
    path("register/", register_view, name="register"),  
    path("login/", login_view, name="login"),  
    path("logout/", logout_view, name="logout"),  
    path("translate/", translate_text, name="translate"),  
    path("dashboard/", dashboard, name="dashboard"),  #  Add dashboard route
    path("translator/", include("translator.urls")),  #  Ensure app-level URLs are included
]