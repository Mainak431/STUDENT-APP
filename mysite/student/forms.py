from django import forms
from .models import Subwise_marks,Course
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,DeleteView



class MarksForm(forms.ModelForm):
    class Meta:
        model = Subwise_marks
        fields = ('EnrollmentID', 'C_ID', 'Marks',)
        labels = {
            'EnrollmentID': ('Enrollment ID'),
            'C_ID': ('Course ID'),
            'Marks': ('Marks'),
        }


