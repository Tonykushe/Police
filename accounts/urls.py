from django.urls  import path
from accounts.views import *
from django.contrib.auth.views import logout


app_name = 'accounts'

urlpatterns = [
        path('', home, name="home"),
        path('login', login_view, name="login"),
        path('logout', logout, {'template_name' : 'accounts/logout.html'}, name='logout'),
        path('signup', signup, name='signup'),
        path('profile', view_profile, name='profile'),
        path('profile/edit', edit_profile, name='edit_profile'),
        path('change-password/', change_password, name='edit_password'),



    
]