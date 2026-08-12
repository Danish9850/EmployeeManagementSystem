from django.urls import  path
from . views import *

urlpatterns = [
    path("",profile,name="profile"),
    path("edit/",edit_profile, name="edit_profile"),
    path("change-password/", change_password, name="change_password"),
]