from django.urls  import path
from accounts.views import *
from django.contrib.auth.views import logout


app_name = 'accounts'

urlpatterns = [
        path('', home, name="home"),
        path('login', login_view, name="login"),
        path('logout', logout, {'template_name' : 'accounts/logout.html'}, name='logout'),
        path('signup', signup, name='signup'),
        path('profile', profile, name='profile'),
        path('profile/edit', editprofile, name='edit_profile'),


    
]