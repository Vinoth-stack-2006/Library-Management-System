# yourapp/forms.py
from django import forms
from .models import Newspaper

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Select Excel/CSV file")

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['brand', 'language', 'publish_date', 'file']
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'})  # date picker
        }

from django import forms
from .models import PurchaseRequest

class PurchaseRequestForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequest
        fields = ['hod_name', 'department', 'book_title', 'author', 'publisher', 'year', 'reason']
        widgets = {
            'department': forms.HiddenInput(),
            'reason': forms.HiddenInput(),
        }
    
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        # Make all fields required
        self.fields['hod_name'].required = True
        self.fields['department'].required = True
        self.fields['book_title'].required = True
        self.fields['author'].required = True
        self.fields['publisher'].required = True
        self.fields['year'].required = True
        self.fields['reason'].required = True

        # Add Bootstrap classes and placeholder text to non-hidden fields
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.HiddenInput):
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label
                })