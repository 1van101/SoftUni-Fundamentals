from django.shortcuts import render, redirect

# from my_plant_app.web.context_processors import get_profile
from my_plant_app.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from my_plant_app.web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist as ex:
        return None


def get_plant(id):
    plant = Plant.objects.filter(id=id).get()
    return plant


# COMMON
def show_home_page(request):
    return render(request, 'common/home-page.html')


def show_catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'common/catalogue.html', context=context)


# PROFILE
def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context=context)


def details_profile(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }
    return render(request, 'profile/profile-details.html', context=context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home page')

    return render(request, 'profile/delete-profile.html')


# PLANTS
def create_plant(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plant/create-plant.html', context)


def details_plant(request, plant_id):
    plant = get_plant(plant_id)
    context = {
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, plant_id):
    plant = get_plant(plant_id)
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, plant_id):
    plant = get_plant(plant_id)
    form = PlantDeleteForm(instance=plant)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/delete-plant.html', context=context)
