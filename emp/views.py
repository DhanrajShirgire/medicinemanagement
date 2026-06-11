from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def home(request):
    music_records = Musician.objects.all()

    context = {
        'music_records': music_records
    }

    return render(request, 'emp/home.html', context)


def add_musician(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        instrument = request.POST.get('instrument')
        profile_image = request.FILES.get('profile_photo')
        print(profile_image)
        Musician.objects.create(
            first_name=first_name,
            last_name=last_name,
            instrument=instrument,
            image=profile_image
        )

        return redirect('musician_list')

    return render(request, 'emp/add_musician.html')




def musician_list(request):
    musicians = Musician.objects.all()

    context = {
        'musicians': musicians
    }

    return render(request, 'emp/musician_list.html', context)