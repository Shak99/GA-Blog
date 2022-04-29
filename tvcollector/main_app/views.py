from django.shortcuts import render, redirect
from .models import TvHost, TvHost, Tvlist
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StudioForm
# import logging
# logger = logging.getLogger(__name__)


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
    studio_form = StudioForm()
    hosts_show_doesnt_have = TvHost.objects.exclude(
        id__in=tvlist.tv_hosts.all().values_list('id'))
    return render(request, 'tv/detail.html', {'tvlist': tvlist, 'id': tvlist.id, 'studio_form': studio_form, 'tvhosts': hosts_show_doesnt_have})

def add_studio(request, tv_id):
      form = StudioForm(request.POST)
      if form.is_valid():
          new_studio = form.save(commit=False)
          new_studio.tv_id = tv_id
          new_studio.save()
      return redirect('detail', tv_id = tv_id)
  
def assoc_tvhost(request, tv_id, tvhost_id):
    Tvlist.objects.get(id=tv_id).tv_hosts.add(tvhost_id)
    return redirect('detail', tv_id=tv_id)

def unassoc_tvhost(request, tv_id, tvhost_id):
    Tvlist.objects.get(id=tv_id).tv_hosts.remove(tvhost_id)
    return redirect('detail', tv_id=tv_id)

class TvHostList(ListView):
    model = TvHost
    
class TvHostCreate(CreateView):
    model = TvHost
    fields = '__all__'
    
class TvHostUpdate(UpdateView):
    model = Tvlist
    fields = ['name', 'host_type']
    
class TvHostDelete(DeleteView):
    model = TvHost
    success_url = '/tvhost/'
