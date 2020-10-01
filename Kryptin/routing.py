from django.conf.urls import url
from django.urls import path, include

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from api.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': 
        URLRouter(
            [
                path('api/user/chat/', ChatConsumer)
            ]
        )
})