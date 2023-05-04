from django.urls import path

from accounts import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path(
        "reset-password/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "reset-done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset-successful",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
