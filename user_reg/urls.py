from django.urls import  re_path
from user_reg import views

urlpatterns=[
     re_path('user_reg/',views.user_reg),
     re_path('manage_user/',views.manage_user),
     re_path('view_blocked_user/',views.view_blocked_user),
     re_path('admin_view_user/',views.admin_view_user),
     re_path('approve_user/(?P<abc>\w+)',views.approve_user,name='approve_user'),
     re_path('reject_user/(?P<cdf>\w+)',views.reject_user,name='reject_user'),
     re_path('blkuser/(?P<idd>\w+)',views.blckuser,name='blkuser'),
     re_path('edit_profile/',views.edit_profile),
     re_path('edit_username/',views.edit_username),
     re_path('edit_email/',views.edit_email),
     re_path('edit_password/',views.edit_password),
     re_path('edit_phno/',views.edit_phno),
     re_path('admin_view_blocked_users/',views.admin_view_blocked_users),
     re_path('unblock/(?P<aa>\w+)',views.unblock,name='unblock')
]
