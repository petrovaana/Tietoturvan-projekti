from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name",)
        labels = {"name": "Tehtävä"}
        widgets = {
            "name": forms.TextInput(
                attrs={"autofocus": True, "maxlength": Task._meta.get_field("name").max_length}
            )
        }
