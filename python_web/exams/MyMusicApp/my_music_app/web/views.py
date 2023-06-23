from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from my_music_app.web.templatetags.custom_tags import get_profile, get_albums, get_album


# COMMON---------------------

def show_home_page(request):
    profile = get_profile()
    albums = get_albums()

    if profile:
        return render(request, 'common/home-with-profile.html', {'albums': albums})

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,

    }
    return render(request, 'common/home-no-profile.html', context=context)


# ALBUM----------------------

def add_album(request):
    form = AlbumCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'album/add-album.html', context=context)


def edit_album(request, pk):
    album = get_album(pk)

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)

        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'album': album,
        'form': form
    }
    return render(request, 'album/edit-album.html', context=context)


def details_album(request, pk):
    album = get_album(pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def delete_album(request, pk):
    album = get_album(pk)
    form = AlbumDeleteForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')

    context = {
        'album': album,
        'form': form
    }
    return render(request, 'album/delete-album.html', context=context)


# PROFILE----------------------

def details_profile(request):
    profile = get_profile()
    albums = get_albums()
    context = {
        'profile': profile,
        'albums_count': len(albums)
    }

    return render(request, 'profile/profile-details.html', context=context)


def delete_profile(request):
    profile = get_profile()
    albums = get_albums()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')