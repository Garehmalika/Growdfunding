from django.urls import re_path 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    user_login,
    signup,
    user_logout,
    EditProfile,
    profile,
    emailPasswordReset,
    ResetPasswordLink,
    ResetPassword,
    deleteAccount,
)

urlpatterns = [
    path('login', user_login, name="login"),
    path('register', signup, name="register"),
    path("logout", user_logout, name="logout"),
    path("profile", profile, name="profile"),
    path('edit/profile', EditProfile, name="editProfile"),
    path('emailReset', emailPasswordReset, name="emailReset"),
    re_path(r'^ResetPasswordLink/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,18})/$',
            ResetPasswordLink, name='ResetPasswordLink'),
    re_path(r'^ResetPasswordLink/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)/$', 
        ResetPasswordLink, name='ResetPasswordLink'),
    path('DeleteAccount', deleteAccount, name="deleteAccount"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
