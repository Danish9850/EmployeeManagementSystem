from django.urls import path
from . views import *

urlpatterns = [
    path("list/", leave_list, name="leave_list"),
    path("apply/", apply_leave, name="apply_leave"),
    path("detail/<int:id>/", leave_detail, name="leave_detail"),
    path("approve/<int:leave_id>/", approve_leave, name="approve_leave"),
    path("reject/<int:leave_id>/", reject_leave, name="reject_leave"),
    path("edit/<int:id>/", edit_leave, name="edit_leave"),
]