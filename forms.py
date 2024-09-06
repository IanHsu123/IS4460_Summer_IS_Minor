from django import forms
from u_parking.models import Vehicle,Driver,Permit

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class PermitForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = '__all__'