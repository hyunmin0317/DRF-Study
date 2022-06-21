from django.shortcuts import render, get_object_or_404

from photo.models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    context = {'photos':photos}
    return render(request, 'photo/photo_list.html', context)


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    context = {'photo': photo}
    return render(request, 'photo/photo_detail.html', context)