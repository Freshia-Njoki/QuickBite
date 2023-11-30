from django import forms
from yummyapp.models import ImageModel
#
# class EmpForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['name', 'email', 'phoneNo']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'description', 'price']