from django.urls import path, reverse_lazy
from .views import logout_view, register_view, login_view, dashboard, my_course, profile_edit
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetForm

urlpatterns = [
    # path('', LoginView.as_view(template_name='account/login.html'), name='login')
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    #profile
    path('dashboard/', dashboard, name='dashboard'),
    path('my_course/', my_course, name='my_course'),
    path('profile_edit/', profile_edit, name='profile_edit'),

    #change_password
    path('change_password/',
         PasswordChangeView.as_view(template_name='account/change_password/password_change_form.html',
                                    success_url=reverse_lazy('account:change_password_done')),
         name='change_password'),
    path('change_password/done/',
         PasswordChangeDoneView.as_view(template_name='account/change_password/password_change_done.html'),
         name='change_password_done'),

    #forget_password
    path('forget_password/',
         PasswordResetView.as_view(template_name='account/forget_password/password_reset_form.html',
                                   email_template_name='account/forget_password/password_reset_email.html',
                                   success_url=reverse_lazy("account:forget_password_done")),
         name='forget_password'),

    path('forget_password/done/',
         PasswordResetDoneView.as_view(template_name='account/forget_password/password_reset_done.html'),
         name='forget_password_done'),

    path('forget_password/confirm/<str:uidb64>/<str:token>/',
         PasswordResetConfirmView.as_view(template_name='account/forget_password/password_reset_confirm.html',
                                          success_url=reverse_lazy("account:forget_password_complete")),
         name='forget_password_confirm'),

    path('forget_password/complete/',
         PasswordResetCompleteView.as_view(template_name='account/forget_password/password_reset_complete.html'),
         name='forget_password_complete'),

]