from django.shortcuts import get_list_or_404, render

from image_gallery.models import Image

def index(request):
    image_list = get_list_or_404(Image, showOnFrontPage=True)
    return render(request, 'kd_dot_net/index.html', { 
        "image_list": image_list,
        "image_ids": [image.id for image in image_list]
    })

def about(request):
    return render(request, 'kd_dot_net/about.html')

def portfolio(request):
    image_list = Image.objects.all()
    return render(request, 'kd_dot_net/portfolio.html', { 
        "image_list": image_list,
        "image_ids": [image.id for image in image_list]
    })

def contact(request):
    return render(request, 'kd_dot_net/contact.html')