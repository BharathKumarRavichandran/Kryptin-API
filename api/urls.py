from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect

from api.views.User import UserStatusView, UserChatView, UserAuthView

app_name = 'api'

urlpatterns = [

    url('user/login/', UserAuthView.LoginFormView.as_view(), name='user-login'),
    url('user/register/', UserAuthView.RegisterFormView.as_view(), name='user-register'),
    url('user/logout/', UserAuthView.LogoutView.as_view(), name='user-logout'),

    url('user/usernameavailability/', UserAuthView.UsernameAvailabilityView.as_view(), name='username-availability'),

    url('user/getusername/', UserAuthView.getUsernameView.as_view(), name='get-username'),

    url('user/online/get/', UserStatusView.GetOnlineView.as_view(), name='get-online'),
    url('user/online/put/', UserStatusView.PutOnlineView.as_view(), name='put-online'),

    url('user/offline/put/', UserStatusView.PutOfflineView.as_view(), name='put-offline'),

    url('user/chat/retrieve', UserChatView.RetrieveChatMessageView.as_view(), name='chat-retrieve')

]