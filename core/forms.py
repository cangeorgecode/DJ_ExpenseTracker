from django import forms
from core.models import Expense

class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date_created', 'item', 'cost', 'category', 'receipt', 'status')
        widgets = {
            'date_created': forms.widgets.DateInput(attrs={'type': 'date'}),
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
        self.fields['category'].empty_label = 'meal'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].help_text = ''

        self.fields['receipt'].label = ''
        self.fields['receipt'].widget.attrs['class'] = 'form-control'
        self.fields['receipt'].widget.attrs['placeholder'] = 'Category'
        self.fields['receipt'].help_text = ''

        self.fields['status'].label = ''
        self.fields['status'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['placeholder'] = 'Category'
        self.fields['status'].help_text = ''