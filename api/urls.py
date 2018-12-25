from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.shortcuts import redirect
from api.views import UserView

urlpatterns = [

    url('user/online/get/', UserView.GetOnlineView.as_view(), name='get-online'),
    url('user/online/put/', UserView.PutOnlineView.as_view(), name='put-online'),

]