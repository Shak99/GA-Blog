from django.db import models


# Create your models here.
class Tvlist(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    seasons = models.IntegerField()
    description = models.CharField(max_length=350)
    status = models.CharField(max_length=250)
    
    def tv_index(request):
        shows = Tvlist.objects.all()
        return render(request, 'tv/index.html', {'shows': shows})