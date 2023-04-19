from django.urls import  re_path
from friends import views

urlpatterns = [
     re_path(r'^search_friends/',views.search_friends),
     re_path(r'^send_friend_request/',views.send_friend_request),
     re_path(r'^manage_friend_request/',views.manage_friend_request),
     re_path(r'^view_friends_list/',views.view_friends_list),
     re_path(r'^chat_with_friends/',views.chat_with_friends),
     re_path(r'^send_request/(?P<abc>\w+)',views.send_request,name='abcdef'),
     re_path(r'^manage_friend_request/', views.manage_friend_request),
     re_path(r'^accept_friend/(?P<abc>\w+)',views.accept_friend,name='accept_friend'),
     re_path(r'^reject_friend/(?P<cdf>\w+)',views.reject_friend,name='reject_friend'),
     re_path(r'^search_result/',views.search_result),
     re_path(r'^search_send_request/(?P<df>\w+)',views.search_send_request,name='aaaaaaaaaa'),
     re_path('already_friend/',views.already_friend),
     re_path('view_blocked_friends/',views.view_blocked_friends,name='block_user'),
    # url('block_your_friends/', views.block_your_friends),

    ]
