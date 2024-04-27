from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'title', 'specialization', 'experience_years', 'hospital_affiliation', 'email', 'phone_number']

        # 如果医生与内置用户模型关联，需要添加以下内容
        # fields = ['user', 'specialization', 'experience_years', 'hospital_affiliation', 'email', 'phone_number']
        # widgets = {
        #     'user': forms.HiddenInput(),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['title'].label = 'Title (optional)'
        self.fields['specialization'].label = 'Specialization'
        self.fields['experience_years'].label = 'Experience Years'
        self.fields['hospital_affiliation'].label = 'Hospital Affiliation'
        self.fields['email'].label = 'Email'
        self.fields['phone_number'].label = 'Phone Number'

        # 如果医生与内置用户模型关联，需要添加以下内容
        # self.fields['user'].label = 'User'