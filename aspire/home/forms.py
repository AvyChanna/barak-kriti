from django import forms
from aspire.home.models import Course


class NameForm(forms.Form):
    pdf = forms.FileField(max_length=100 , required=True)
    title = forms.CharField(widget=forms.Textarea , required=True)
    c = Course.objects.all().values_list('name')
    c = [u[0] for u in c]
    course = forms.ChoiceField(choices=c , required=True)


