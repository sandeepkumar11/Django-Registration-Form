from django.urls import path
from . import views
from .forms import ChangePasswordForm, ResetPasswordForm, PasswordSetForm

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(next_page='/login/'),name='logout'),

    path('change-password/',views.PasswordChangeView.as_view(template_name="LogInOut/change-password.html",form_class=ChangePasswordForm),name='change-password'),

    path('password-change-done/',views.PasswordChangeDoneView.as_view(template_name="LogInOut/password-change-done.html"),name="password_change_done"),

    path('reset-password/',views.PasswordResetView.as_view(template_name="LogInOut/reset-password.html",form_class=ResetPasswordForm),name='reset-password'),

    path('password-reset-confirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='LogInOut/reset-password-confirm.html',form_class=PasswordSetForm),name='password_reset_confirm'),

    path('password-reset-done/',views.PasswordResetDoneView.as_view(template_name='LogInOut/reset-password-done.html'),name='password_reset_done'),

    path('password-reset-complete/',views.PasswordResetCompleteView.as_view(template_name='LogInOut/password-reset-complete.html'),name='password_reset_complete'),
]