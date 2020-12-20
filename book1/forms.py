from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels = {
            'full_name':'Full Name',
            'emp_code':'Employee Code'
        }

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = "select"