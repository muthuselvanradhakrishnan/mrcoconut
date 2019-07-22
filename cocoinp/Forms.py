from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class InputForm(forms.Form):
    hotel_name = forms.CharField()
    hotel_address = forms.CharField()
    mobile_number = forms.IntegerField()
    qty_required = forms.IntegerField()
    date_required = forms.DateField(widget=DateInput)