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
from django.conf.urls import url
from workshop_app.views import (
    RoomListView,
    RoomDetailView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
    ReservationCreateView,
    ReservationListView,
    ReservationDetailView,
    ReservationDeleteView,
    SearchFormView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RoomListView.as_view(), name='room-list-view'),
    url(r'^room/new/$', RoomCreateView.as_view(), name='room-create-view'),
    url(r'^room/(?P<id>(\d)+)/$', RoomDetailView.as_view(), name='room-detail-view'),
    url(r'^room/modify/(?P<id>(\d)+)/$', RoomUpdateView.as_view(), name='room-update-view'),
    url(r'^room/delete/(?P<id>(\d)+)/$', RoomDeleteView.as_view(), name='room-delete-view'),
    url(r'^reservation/$', ReservationListView.as_view(), name='reservation-list-view'),
    url(r'^reservation/new/$', ReservationCreateView.as_view(), name='reservation-create-view'),
    url(r'^reservation/(?P<id>(\d)+)/$', ReservationDetailView.as_view(), name='reservation-detail-view'),
    url(r'^reservation/delete/(?P<id>(\d)+)/$', ReservationDeleteView.as_view(), name='reservation-delete-view'),
    url(r'^search/$', SearchFormView.as_view(), name='search-view'),
]
