from models import Trip
from django import forms

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('notes',)

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)

        self.fields['date'].widget.attrs['placeholder'] = "Date of trip"
        self.fields['odometer_start'].widget.attrs['placeholder'] = "Beginning odometer reading"
        self.fields['odometer_end'].widget.attrs['placeholder'] = "Ending odometer reading"
        self.fields['reason'].widget.attrs['placeholder'] = "Reason for trip (optional)"

        self.fields['date'].widget.attrs['data-mini'] = "true"
        self.fields['odometer_start'].widget.attrs['data-mini'] = "true"
        self.fields['odometer_end'].widget.attrs['data-mini'] = "true"
        self.fields['reason'].widget.attrs['data-mini'] = "true"

        self.fields['date'].widget.input_type = "date"
        self.fields['odometer_start'].widget.input_type = "tel"
        self.fields['odometer_end'].widget.input_type = "tel"
        self.fields['reason'].widget.input_type = "text"

