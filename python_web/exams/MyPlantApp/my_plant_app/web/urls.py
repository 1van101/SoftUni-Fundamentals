from django.urls import path, include

from my_plant_app.web.views import show_home_page, create_profile, details_profile, edit_profile, delete_profile, \
    create_plant, details_plant, edit_plant, delete_plant, show_catalogue

urlpatterns = (
    path('', show_home_page, name='home page'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('create/', create_plant, name='create plant'),
    path('details/<plant_id>/', details_plant, name='details plant'),
    path('edit/<plant_id>/', edit_plant, name='edit plant'),
    path('delete/<plant_id>/', delete_plant, name='delete plant'),
    path('catalogue/', show_catalogue, name='catalogue'),

)
