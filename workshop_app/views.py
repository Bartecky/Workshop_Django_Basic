import datetime
from django.shortcuts import get_object_or_404, reverse, redirect, render
from .models import Reservation, Room
from .forms import RoomModelForm, ReservationModelForm, SearchForm
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
    View,
)


# Create your views here.
class RoomListView(ListView):
    template_name = 'room-list-view.html'
    queryset = Room.objects.all().order_by('id')


class RoomDetailView(DetailView):
    template_name = 'room-detail-view.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('id')
        return get_object_or_404(Room, id=_id)


class RoomCreateView(CreateView):
    template_name = 'room-create-view.html'
    form_class = RoomModelForm


class RoomUpdateView(UpdateView):
    template_name = 'room-create-view.html'
    form_class = RoomModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)


class RoomDeleteView(DeleteView):
    template_name = 'room-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Room, id=id_)

    def get_success_url(self):
        return reverse('room-list-view')


class ReservationListView(ListView):
    template_name = 'reservation-list-view.html'
    queryset = Reservation.objects.filter(date__gte=datetime.date.today()).order_by('date')


class ReservationCreateView(CreateView):
    template_name = 'reservation-create-view.html'
    form_class = ReservationModelForm

class ReservationDetailView(DetailView):
    template_name = 'reservation-detail-view.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=_id)

class ReservationDeleteView(DeleteView):
    template_name = 'reservation-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id_)

    def get_success_url(self):
        return reverse('reservation-list-view')


class SearchFormView(View):
    def get(self, request):
        form = SearchForm()
        ctx = {
            'form': form,
        }
        return render(request, 'search-view.html', ctx)

    def post(self, request):
        form = SearchForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['min_capacity']
            projector = form.cleaned_data['projector']
            if projector:
                projector = True
            else:
                projector = False
            rooms = Room.objects.filter(name__contains=name).filter(capacity__gte=capacity).filter(pojector_is_available=projector)
            ctx['rooms'] = rooms
            return render(request, 'search-view.html', ctx)
