from django import forms

from my_plant_app.web.models import Profile, Plant


# PROFILE

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    ProfileBaseForm.Meta.fields.append('profile_picture')


# PLANT

class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'image_url': 'Image URL'
        }


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
