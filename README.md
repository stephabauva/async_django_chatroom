# async_django_chatroom
A chatroom using django asynchrously with channels and websockets

pip3 instaal django
pip3 install channels
django-admin startproject core .
python3 manage.py startapp chat
'chat' and 'channels' in INSTALLED_APPS in core/settings
python3 manage.py migrate
create urls.py folder in chat
add path('chat/', include('chat.urls')), and import include to core/urls
add urlpatterns to chat/urls
create 'templates' folder in chat
add index view to chat/views
python3 manage.py runserver 
ERROR --> CommandError: You have not set ASGI_APPLICATION, which is needed to run the server.
|---> add ASGI_APPLICATION = 'core.routing.application' to core/settings
python3 manage.py runserver
ERROR --> AttributeError: module 'chat.views' has no attribute 'room'
|--> add room view to chat/views
python3 manage.py runserver
ERROR -->  Cannot import ASGI_APPLICATION module 'core.routing'
|--> add routing.py file in core to act as the router between ASGI (Daphine) and Consumer(s)
|--> add routing.py file in chat too
add class in consumers.py
add script with chatsocket variable in base.html, after pasting the bootstra boilerplate