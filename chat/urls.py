from django.urls import  re_path
from chat import views

urlpatterns = [
     re_path('chat/(?P<abc>\w+)',views.chat,name='chat'),
     re_path('chat_with_friends/',views.chat_with_friends),
     re_path('view_chat/',views.view_chat)

]
