from games_play_app.web.views import get_profile


def base_context(request):
    return {
        'logged_profile': get_profile(),
    }