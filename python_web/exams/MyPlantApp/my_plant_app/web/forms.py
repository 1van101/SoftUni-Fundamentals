from django import forms

from my_plant_app.web.models import Profile, Plant


# PROFILE
class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['profile_picture']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



# PLANT

class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'plant_type':
                field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
