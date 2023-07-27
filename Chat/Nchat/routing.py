from django.urls import path
from .consumer import ChatConsumer

WS_url_patterns =[
    path('chat/<str:group>',ChatConsumer.as_asgi())
]