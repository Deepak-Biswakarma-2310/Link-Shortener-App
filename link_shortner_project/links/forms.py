from django import forms
from .models import Link
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'url']

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Link', css_class='bg-indigo-600 text-white rounded-md shadow-md hover:shadow-lg hover:bg-indigo-700 transition duration-300 ease-in-out hover:ring-2 hover:ring-indigo-300'))
