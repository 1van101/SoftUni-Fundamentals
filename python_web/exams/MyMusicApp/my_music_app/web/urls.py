from django.urls import path, include

from my_music_app.web.views import show_home_page, add_album, edit_album, details_album, delete_album, details_profile, \
    delete_profile

urlpatterns = (
    path('', show_home_page, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('edit/<pk>/', edit_album, name='edit album'),
        path('details/<pk>/', details_album, name='details album'),
        path('delete/<pk>/', delete_album, name='delete album')
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
)
