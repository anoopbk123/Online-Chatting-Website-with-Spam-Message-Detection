from django.urls import  re_path
from login import views

urlpatterns = [
     re_path('login/',views.login),
    # url('forgot_password/',views.forgot_password)

]
