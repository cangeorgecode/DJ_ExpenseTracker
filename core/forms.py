from django import forms
from core.models import Expense

class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date_created', 'item', 'cost', 'category',)
        widgets = {
            'date_created': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AddExpenseForm, self).__init__(*args, **kwargs)

        self.fields['date_created'].label = ''
        self.fields['date_created'].widget.attrs['class'] = 'form-control'
        self.fields['date_created'].widget.attrs['placeholder'] = 'Date'
        self.fields['date_created'].help_text = ''

        self.fields['item'].label = ''
        self.fields['item'].widget.attrs['class'] = 'form-control'
        self.fields['item'].widget.attrs['placeholder'] = 'Item'
        self.fields['item'].help_text = ''

        self.fields['cost'].label = ''
        self.fields['cost'].widget.attrs['class'] = 'form-control'
        self.fields['cost'].widget.attrs['placeholder'] = 'Cost'
        self.fields['cost'].help_text = ''

        self.fields['category'].label = ''
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['placeholder'] = 'Category'
        self.fields['category'].help_text = ''
