from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('applications.authentication.urls')),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]