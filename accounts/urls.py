from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("settings/<slug:slug>/", views.settings, name="settings"),
    path("users/students/list/", views.student_list, name="student-list"),
    path("remove-student/<int:pk>/", views.delete_student, name="delete-student"),
    path("users/staffs/list/", views.staff_list, name="staff-list"),
    path("remove-staff/<int:pk>/", views.delete_staff, name="delete-staff"),
    path("users/", views.manage_users, name="manage-users"),
    path("users/admin/list", views.admin_list, name="admin-list"),
    path("remove-admin/<int:pk>/", views.delete_admin, name="remove-admin"),
]
