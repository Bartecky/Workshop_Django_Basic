from django import forms
from .models import Room, Reservation
from django.core.validators import ValidationError
import datetime

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'capacity',
            'pojector_is_available',
            'is_active',
        ]


def validate_date(date):
    if date < datetime.datetime.now().date():
        raise ValidationError('Wrong date')


class ReservationModelForm(forms.ModelForm):
    comment = forms.CharField(required=False)
    date = forms.DateField(validators=[validate_date], initial=datetime.date.today())

    class Meta:
        model = Reservation
        fields = [
            'date',
            'room',
            'comment',
        ]


class SearchForm(forms.Form):
    name = forms.CharField(label='Room Name', max_length=32, required=False)
    min_capacity = forms.IntegerField(label='Min capacity', initial=25)
    # day = forms.DateField(required=False, initial=datetime.today())
    projector = forms.BooleanField(label='Projector', required=False, initial=True)
