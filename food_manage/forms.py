import bootstrap_datepicker_plus as datetimepicker
from django import forms
from . models import Data
 
class FoodForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('name', 'num','term')
        labels={
           'name':'名前',
           'num':'個数',
           'term':'賞味期限',
           }

        widgets = {
            'term': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'ja',
                     'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }