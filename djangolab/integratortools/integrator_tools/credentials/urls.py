from django.urls import path 

from . import views 

urlpatterns = [
    path("",views.cred_home,name="credentials-home"),
    path("user",views.user_credential,name="user-credential"),
]
