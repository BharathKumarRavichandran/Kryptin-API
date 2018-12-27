from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect
from api.views.User import UserStatusView

app_name = 'api'

urlpatterns = [

    url('user/online/get/', UserStatusView.GetOnlineView.as_view(), name='get-online'),
    url('user/online/put/', UserStatusView.PutOnlineView.as_view(), name='put-online'),

]