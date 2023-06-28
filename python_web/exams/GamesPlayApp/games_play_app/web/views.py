from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from games_play_app.web.forms import CreateProfileForm, CreateGameForm
from games_play_app.web.mixins import DisabledFormFieldsMixin
from games_play_app.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist as ex:
        return None


# COMMON


class HomePageView(views.TemplateView):
    template_name = 'common/home-page.html'


# GAME

class DashboardGameView(views.ListView):
    template_name = 'common/dashboard.html'
    model = Game


class CreateGameView(views.CreateView):
    form_class = CreateGameForm
    template_name = 'game/create-game.html'
    success_url = reverse_lazy('dashboard game')


class DetailsGameView(views.DetailView):
    model = Game
    template_name = 'game/details-game.html'


class EditGameView(views.UpdateView):
    model = Game
    form_class = modelform_factory(
        model,
        fields='__all__'
    )
    template_name = 'game/edit-game.html'
    success_url = reverse_lazy('dashboard game')


class DeleteGameView(DisabledFormFieldsMixin, views.DeleteView):
    model = Game
    form_class = modelform_factory(
        model,
        fields='__all__',
    )

    template_name = 'game/delete-game.html'
    success_url = reverse_lazy('dashboard game')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs


# PROFILE

class CreateProfileView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('home page')


class DetailsProfileView(views.DetailView):
    model = Profile
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        games = Game.objects.all()
        average_rating = sum([x.rating for x in games]) / len(games) if games else 0.0

        context['games'] = games
        context['average_rating'] = average_rating 

        return context



def edit_profile(request):
    pass


def delete_profile(request):
    pass
