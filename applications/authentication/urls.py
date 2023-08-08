from dj_rest_auth.registration.views import RegisterView , VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetConfirmView, PasswordResetView
from django.urls import path, re_path


urlpatterns = [
    path("account-confirm-email/<str:key>/", VerifyEmailView.as_view(), name="account_email_verification_sent"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("profile/", UserDetailsView.as_view(), name="rest_user_details"),
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
        VerifyEmailView.as_view(), name='account_confirm_email'),
]