from django.forms import ModelForm
from main.models import KambingEntry

class KambingEntryForm(ModelForm):
    class Meta:
        model = KambingEntry
        fields = ["name", "price", "description"]