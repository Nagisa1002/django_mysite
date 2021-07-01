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