from crispy_forms import helper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Field, Layout, Submit
from django import forms
from django.forms import ModelForm

from .models import Quote, Tag, Author


class QuoteSearchForm(forms.Form):
    text = forms.CharField(required=False)
    author = forms.ModelChoiceField(Author.objects.order_by('name'), required=False)
    tag = forms.ModelChoiceField(Tag.objects.order_by('name'), required=False)


class QuoteCreateForm(forms.ModelForm):
    text = forms.CharField(max_length=2500, widget=forms.Textarea)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Quote
        fields = ('text', 'tag')

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper.form_id = 'id-quoteform'
        #     self.helper.layout = Layout
        #     (
        #         Field('text', rows="3", css_class='form-control mb-3'),
        #         Field('tags', css_class='form-control mb-3'),
        #         FormActions(
        #             Submit('save_changes', 'Save changes', css_class="btn-primary"),
        #             Submit('cancel', 'Cancel')
        #         )
        #     )