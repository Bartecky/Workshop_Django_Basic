from django import forms
from .models import Room, Reservation


class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'capacity',
            'pojector_is_available',
            'is_active',
        ]


class ReservationModelForm(forms.ModelForm):
    date = forms.DateField()
    comment = forms.CharField(required=False)

    class Meta:
        model = Reservation
        fields = [
            'date',
            'room',
            'comment',
        ]
