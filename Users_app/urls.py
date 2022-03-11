from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, SetPasswordForm, Sign_In_Form
from .views import (index, user_account_info, user_account_security, user_account_wishlist, 
                    user_account_reviews, about_us, contact_us, contact_us_done, help_center, 
                    sign_out)

urlpatterns = [
    path('', index, name='index-page'),
    path('account-info', user_account_info, name='user-account-info-page'),
    path('account-security', user_account_security, name='user-account-security-page'),
    path('account-wishlist', user_account_wishlist, name='user-account-wishlist-page'),
    path('account-reviews', user_account_reviews, name='user-account-reviews-page'),
    path('about-us', about_us, name='about-us-page'),
    path('contact-us', contact_us, name='contact-us-page'),
    path('contact-us-done', contact_us_done, name='contact-us-done-page'),
    path('help-center', help_center, name='help-center-page'),
    path('sign-out', sign_out, name='sign-out-page'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="password-reset.html", form_class=UserPasswordResetForm, extra_context={'password_reset':True}), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-done.html", extra_context={'password_reset':True}), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html", form_class=SetPasswordForm, extra_context={'password_reset':True}), name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html", extra_context={'sign_in_form':Sign_In_Form(), 'password_reset':True}), name='password_reset_complete'),

]

# data  venture
# davinci
# svikratani
# utkrista
# statistech
# data megician
