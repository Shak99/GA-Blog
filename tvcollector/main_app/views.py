from django.shortcuts import render
from .models import Tvlist
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
from django.http import HttpResponse


class TvList(ListView):
    model = Tvlist
    
class TvCreate(CreateView):
    model = Tvlist
    fields = '__all__'
    success_url = '/tv/'
    
class TvUpdate(UpdateView):
    model = Tvlist
    fields = ['year', 'genre', 'seasons', 'description', 'status']
    
class TvDelete(DeleteView):
    model = Tvlist
    success_url = '/tv/'

# Define the home view
def home(request):
  return HttpResponse('<h1>1 Home page</h1>')

def about(request):
    return render(request, 'about.html')

def tvshow(request):
    tvlist = Tvlist.objects.all()
    return render(request, 'tv/index.html', {'tvlist': tvlist})

def detail(request, tv_id):
    tvlist = Tvlist.objects.get(id=tv_id)
    return render(request, 'tv/detail.html', {'tvlist': tvlist, 'id': tvlist.id})
