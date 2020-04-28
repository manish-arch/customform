from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['TMC_NO'].error_messages = {
            "invalid": u"Must Enter a valid TMC NO",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('TMC_NO')
