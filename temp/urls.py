from django.urls import  re_path
from temp import views


urlpatterns = [
         re_path('userhome/',views.user_home),
         re_path('admin_home/',views.admin_home),
         re_path('login/',views.login)

]