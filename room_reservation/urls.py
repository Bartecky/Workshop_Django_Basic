"""room_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workshop_app.views import RoomListView, \
                                RoomDetailView, \
                                RoomCreateView, \
                                RoomUpdateView, \
                                RoomDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RoomListView.as_view(), name='home'),
    path('room/new', RoomCreateView.as_view()),
    path('room/<int:id>', RoomDetailView.as_view()),
    path('room/modify/<int:id>', RoomUpdateView.as_view()),
    path('room/delete/<int:id>', RoomDeleteView.as_view()),
]
