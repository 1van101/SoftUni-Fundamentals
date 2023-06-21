from my_plant_app.web.models import Profile, Plant


from my_plant_app.web.views import get_profile


def base_context(request):
    return {
        'logged_profile': get_profile(),
    }
