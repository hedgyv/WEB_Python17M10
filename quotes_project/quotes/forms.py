from django.forms import ModelForm, CharField, TextInput
from .models import Quote

class QuoteForm(ModelForm):

    quote = CharField(min_length=5, max_length=500, required=True, widget=TextInput())
    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    birthday = CharField(min_length=5, max_length=50, required=False, widget=TextInput())
    location = CharField(min_length=10, max_length=50, required=False, widget=TextInput())
    description = CharField(min_length=10, max_length=500, required=False, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author','birthday', 'location','description']
        
        