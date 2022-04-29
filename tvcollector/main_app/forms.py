from django.forms import ModelForm
from .models import Studio

class StudioForm(ModelForm):
  class Meta:
    model = Studio
    fields = ['name', 'prem_date', 'country_origin']