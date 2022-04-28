from unittest.mock import DEFAULT
from django.db import models
# Import the reverse function
from django.urls import reverse


# Create your models here.
class Tvlist(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    seasons = models.IntegerField()
    description = models.CharField(max_length=350)
    status = models.CharField(max_length=250)
    
    # def tv_index(request):
    #     shows = Tvlist.objects.all()
    #     return render(request, 'tv/index.html', {'shows': shows})
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tv_id': self.id})

STUDIOS = (
    ('A', 'Universal Studios'),
    ('B', 'Paramount'),
    ('C', 'Netflix'),
    ('D', 'Dreamworks'),
    ('E', 'Disney'),
    ('F', 'Lionsgate'),
    
)   
   
class Studio(models.Model):
    name = models.CharField(
        max_length=250,
        choices = STUDIOS,
        default = STUDIOS[0][0]
        )
    prem_date = models.DateField('Premiere Date')
    country_origin = models.CharField(max_length=250)
    show = models.ForeignKey(Tvlist, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_Studio_display()} premiered this show in {self.country_origin} on {self.prem_date}"
    