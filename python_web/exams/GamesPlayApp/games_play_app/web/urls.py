from django.urls import path, include

from games_play_app.web.views import EditGameView, DeleteGameView, DetailsProfileView, \
    edit_profile, delete_profile, HomePageView, CreateProfileView, DashboardGameView, CreateGameView, DetailsGameView

urlpatterns = (
    path('', HomePageView.as_view(), name='home page'),
    path('dashboard/', DashboardGameView.as_view(), name='dashboard game'),
    path('game/', include([
        path('create/', CreateGameView.as_view(), name='create game'),
        path('details/<pk>/', DetailsGameView.as_view(), name='details game'),
        path('edit/<pk>/', EditGameView.as_view(), name='edit game'),
        path('delete/<pk>/', DeleteGameView.as_view(), name='delete game'),
    ])),
    path('profile/', include([
        path('create/', CreateProfileView.as_view(), name='create profile'),
        path('details/', DetailsProfileView.as_view(), name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)
