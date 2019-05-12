from django import forms
from .models import Short_Course,Music_Production,Comment,Studio_Session
from django.forms import Textarea


class Studio_SessionForm(forms.ModelForm):
    class Meta:
        model = Studio_Session
        fields = ['full_name','phone_number','email','booked_as','start_date','end_date',]
        # fields = ['fullName','phoneNumber',]

    def __init__(self, *args, **kwargs):
        super(Studio_SessionForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control'

        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
       
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['booked_as'].widget.attrs['readonly']= True
        self.fields['booked_as'].widget.attrs['class'] = 'form-control'

        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['readonly']= True

        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['readonly']= True




class Music_ProductionForm(forms.ModelForm):
    class Meta:
        model = Music_Production
        fields=['full_name','phone_number','email','booked_as','start_date','end_date']
        # fields = ['fullName','phoneNumber',]
    def __init__(self,*args,**kwargs):
        super(Music_ProductionForm, self).__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control'

        self.fields['phone_number'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['readonly'] = True

        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['readonly'] = True

        self.fields['booked_as'].widget.attrs['class'] = 'form-control'

class Short_CourseForm(forms.ModelForm):
    class Meta:
        model= Short_Course
        fields= ('full_name','phone_number','email','course','start_date','end_date',)
    def __init__(self,*args,**kwargs):
        super(Short_CourseForm, self).__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control'

        self.fields['phone_number'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['readonly'] = True

        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['readonly'] = True

        self.fields['course'].widget.attrs['class'] = 'form-control'

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
