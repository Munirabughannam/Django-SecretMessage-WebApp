from django.urls import path
from . import views


urlpatterns = [
    path('', views.messageprompt, name='base'),
    path('reveal', views.generation_view, name='generation'),
    path('reveal/message/<str:secret_id>', views.reveal_message, name='reveal'),
]
