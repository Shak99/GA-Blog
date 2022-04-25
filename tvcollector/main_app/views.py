from django.shortcuts import render
from .models import Tvlist

# Create your views here.
from django.http import HttpResponse


# class Tvlist:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, title, year, genre, seasons, description, status):
#     self.title = title
#     self.year = year
#     self.genre = genre
#     self.seasons = seasons
#     self.description = description
#     self.status = status

# showlist = [
#   Tvlist('Charmed', 1998, 'Fantasy/Sci-Fi', 8, 'A trio of sisters, known as The Charmed Ones, the most powerful good witches of all time, who use their combined "Power of Three" to protect innocent lives from evil beings such as demons and warlocks.', 'Completed!'),
#   Tvlist('90210', 2008, 'Drama', 5, "A reboot of the 90's show Beverly Hills, 90210, the show follows the lives of several wealthy students attending West Beverly Hills High School in Beverly Hills, California", 'Still working on it...'),
#   Tvlist('A Different World', 1987, 'Comedy', 5, 'A spin-off of the Cosy Show, focuses on Denise and other college students attending a historically Black college (HBCU) Hillman College.', 'Completed!'),
#   Tvlist('Switched At Birth', 2011, 'Drama', 5, 'Two teenagers who were switched at birth and grew up in very different environments: one in an affluent suburb, and the other in a working-class neighborhood.', "Didn't Finish"),
# ]

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
    return render(request, 'tv/detail.html', {'tvlist': tvlist})
