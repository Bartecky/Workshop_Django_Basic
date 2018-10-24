from django.shortcuts import render, get_object_or_404
from .models import Reservation, Room
from .forms import RoomModelForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse


# Create your views here.
class RoomListView(ListView):
    template_name = 'room-list.html'
    queryset = Room.objects.all().order_by('id')


class RoomDetailView(DetailView):
    template_name = 'room-details.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)


class RoomCreateView(CreateView):
    template_name = 'room-create.html'
    form_class = RoomModelForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class RoomUpdateView(UpdateView):
    template_name = 'room-create.html'
    form_class = RoomModelForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class RoomDeleteView(DeleteView):
    template_name = 'room-delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_success_url(self):
        return '/'
