from apps.users.views import register_page, send_code_to_email,  register_user, login_page, logout_page
from django.urls import path


urlpatterns = [
    path('register-page', register_page, name='register-page'), 
    path('send_code', send_code_to_email, name='send_code_to_email'),
    path('register-user', register_user, name='register-user'),
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),

]