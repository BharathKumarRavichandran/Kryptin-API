from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect
from api.views.User import UserStatusView, UserChatView

app_name = 'api'

urlpatterns = [

    url('user/usernameavailability/', UserStatusView.UsernameAvailabilityView.as_view(), name='username-availability'),

    url('user/online/get/', UserStatusView.GetOnlineView.as_view(), name='get-online'),
    url('user/online/put/', UserStatusView.PutOnlineView.as_view(), name='put-online'),

    url('user/chat/retrieve', UserChatView.RetrieveChatMessageView.as_view(), name='chat-retrieve')

]