from django.shortcuts import get_object_or_404, reverse
from .models import Reservation, Room
from .forms import RoomModelForm, ReservationModelForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView


# Create your views here.
class RoomListView(ListView):
    template_name = 'room-list.html'
    queryset = Room.objects.all().order_by('id')


class RoomDetailView(DetailView):
    template_name = 'room-details.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)


class RoomCreateView(CreateView):
    template_name = 'room-create.html'
    form_class = RoomModelForm

    def get_success_url(self):
        return reverse('room-list-view')


class RoomUpdateView(UpdateView):
    template_name = 'room-create.html'
    form_class = RoomModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_success_url(self):
        return reverse('room-list-view')


class RoomDeleteView(DeleteView):
    template_name = 'room-delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_success_url(self):
        return reverse('room-list-view')


class ReservationListView(ListView):
    template_name = 'reservation-list.html'
    queryset = Reservation.objects.all().order_by('date')


class ReservationCreateView(CreateView):
    template_name = 'reservation-create.html'
    form_class = ReservationModelForm

    def get_success_url(self):
        return reverse('room-list-view')


class ReservationDeleteView(DeleteView):
    template_name = 'reservation-delete.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id_)

    def get_success_url(self):
        return reverse('reservation-list-view')
