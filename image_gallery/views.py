from django.shortcuts import get_object_or_404, render

from .models import Image

# Create your views here.
def photo(request, photo_id):
    image = get_object_or_404(Image, id=photo_id)
    return render(request, "image_gallery/imageTile.html", { "image": image })

def fullphoto(request, photo_id):
    image = get_object_or_404(Image, id=photo_id)
    return render(request, "image_gallery/fullImage.html", { "image": image })