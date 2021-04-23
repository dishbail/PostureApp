import os 

from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack


from django.urls import path
from django.conf.urls import url
from channels.http import AsgiHandler
from Customer import consumer

websocket_urlPattern=[
    url('ws/polData/',consumer.DashConsumer),
]
application=ProtocolTypeRouter({
    #'http': AsgiHandler(),

    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})