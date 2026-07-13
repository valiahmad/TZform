from django import forms
from .models import Tazkera


class TazkeraForm(forms.ModelForm):

    class Meta:
        model = Tazkera
        fields = "__all__"

        widgets = {
                "services": forms.CheckboxSelectMultiple(),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():

            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs["class"] = "form-control"