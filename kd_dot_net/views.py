from django.shortcuts import render

from image_gallery.models import Image

def index(request):
    try:
        image_list = Image.objects.get(showOnFrontPage=True)
    except Image.DoesNotExist:
        image_list = []
        
    return render(request, 'kd_dot_net/index.html', { 
        "image_list": image_list,
        "image_ids": [image.id for image in image_list],
        "display_type": "uniform" # this is a CSS class forming the 3x3 grid on the homepage
    })

def about(request):
    return render(request, 'kd_dot_net/about.html')

def portfolio(request):
    image_list = Image.objects.all()
    return render(request, 'kd_dot_net/portfolio.html', { 
        "image_list": image_list,
        "image_ids": [image.id for image in image_list],
        "display_type": "ragged" # CSS class forming the random-seeming layout of the portfolio
    })

def contact(request):
    return render(request, 'kd_dot_net/contact.html')
