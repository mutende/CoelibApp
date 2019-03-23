from django import forms
from .models import HireProducer,StudioSession,Comment
from django.forms import Textarea


class HireProducerForm(forms.ModelForm):
    class Meta:
        model = HireProducer
        fields = ['fullName','phoneNumber','producer_name','hire_date','hire_time','duration_days',]
        # fields = ['fullName','phoneNumber',]

    def __init__(self, *args, **kwargs):
        super(HireProducerForm, self).__init__(*args, **kwargs)
        self.fields['fullName'].widget.attrs['class'] = 'form-control'
        self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'
        self.fields['producer_name'].widget.attrs['class'] = 'form-control'

        self.fields['hire_date'].widget.attrs['class'] = 'form-control'
        self.fields['hire_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'

        self.fields['hire_time'].widget.attrs['class'] = 'form-control'
        self.fields['hire_time'].widget.attrs['placeholder'] = 'HH:MM'

        self.fields['duration_days'].widget.attrs['class'] = 'form-control'
        # self.fields['duration_hrs'].widget.attrs['class'] = 'form-control'

class StudioSessionForm(forms.ModelForm):
    class Meta:
        model = StudioSession
        fields=['fullName','phoneNumber','booked_as','start_date',]
        # fields = ['fullName','phoneNumber',]
    def __init__(self,*args,**kwargs):
        super(StudioSessionForm, self).__init__(*args,**kwargs)
        self.fields['fullName'].widget.attrs['class'] = 'form-control'
        self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'

        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'

        self.fields['booked_as'].widget.attrs['class'] = 'form-control'

        # self.fields['starting_time'].widget.attrs['class'] = 'form-control'
        # self.fields['starting_time'].widget.attrs['placeholder'] = '00:00'

class CommentForm(forms.ModelForm):
    #comment = forms.CharField(label="Your Comment", widget=forms.Textarea(attrs={'class':'form-control','cols':4, 'rows':5}))
    class Meta:
        model= Comment
        fields= ['name','email','comment',]
        widgets = {
            'comment': Textarea(attrs={'class':'form-control','cols':4, 'rows':5}),
        }
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
