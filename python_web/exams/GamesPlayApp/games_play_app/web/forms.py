from django import forms

from games_play_app.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput()
        }


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL'
        }

