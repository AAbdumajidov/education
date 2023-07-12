from django import forms
from ..models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': "form-control py-2",
            'id': "name"
        })
        self.fields['email'].widget.attrs.update({
            'class': "form-control py-2",
            'id': "email"
        })
        self.fields['body'].widget.attrs.update({
            'class': "form-control py-2",
            'id': "message",
            'cols': "30",
            'rows': "8",
        })

