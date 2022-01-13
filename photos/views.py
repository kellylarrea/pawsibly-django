from django.shortcuts import render
from .models import photos #import photos model

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    # imports photos and save it in database
    photo = photos.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)