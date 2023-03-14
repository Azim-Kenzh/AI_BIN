from .models import ImageBin
from django.forms import ModelForm


class ImageBinForm(ModelForm):
    class Meta:
        model = ImageBin
        fields = ('image', )
