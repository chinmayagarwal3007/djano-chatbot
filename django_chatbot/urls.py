from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
]
