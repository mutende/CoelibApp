from django import forms
from services.models import Hire_Producer


class HireProducerForm(forms.Form):
    fullName = forms.EmailField(label="Full Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phoneNumber = forms.EmailField(label="Phone Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    producer_name = forms.EmailField(label="Producer Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    hire_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    hire_time = forms.EmailField(label="Time to Hire", widget=forms.TextInput(attrs={'class': 'form-control'}))
    duration_days = forms.EmailField(label="Duration in days", widget=forms.TextInput(attrs={'class': 'form-control'}))
    duration_hrs = forms.EmailField(label="Duration in hours", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # class Meta:
    #     model = Hire_Producer
    #     field = ('fullName', 'phoneNumber', 'producer_name', 'hire_date', 'hire_time', 'duration_days', 'duration_hrs')
    #
    # def __init__(self, *args, **kwargs):
    #     super(HireProducerForm, self).__init__(*args, **kwargs)
    #     self.fields['fullName'].widget.attrs['class'] = 'form-control'
    #     self.fields['fullName'].label = 'Full names'
    #
    #     self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'
    #     self.fields['phoneNumber'].label = 'Phone Number'
    #
    #     self.fields['producer_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['producer_name'].label = 'Producer to hire'
    #
    #     self.fields['hire_date'].widget.attrs['class'] = 'form-control'
    #     self.fields['hire_date'].label = 'Date of hire'
    #
    #     self.fields['hire_time'].widget.attrs['class'] = 'form-control'
    #     self.fields['hire_time'].label = 'Time of hire'
    #
    #     self.fields['duration_days'].widget.attrs['class'] = 'form-control'
    #     self.fields['duration_days'].label = 'Duration in Days'
    #
    #     self.fields['duration_hrs'].widget.attrs['class'] = 'form-control'
    #     self.fields['duration_hrs'].label = 'Duration in hours'
