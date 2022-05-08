from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
# class pgattribute(models.Model):
#     attri1 = models.CharField(max_length=30)
#     attri2 = models.CharField(max_length=30)
#     attri3 = models.CharField(max_length=30)
#     attri9 = models.IntegerField()

class songmodel(models.Model):
    song_model = models.CharField(max_length=90,unique=True)
    slug_field = models.SlugField(max_length=90,unique=True,blank=True)
    class Meta:
        ordering=('song_model',)
        verbose_name='categorry'
        verbose_name_plural='categories'

    def geturl(self):
        return reverse('sng_vw', args=[self.slug_field],)

    def __str__(self):
        return '{}'.format(self.song_model)


class song_details(models.Model):
    song_id = models.IntegerField(primary_key=True,unique=True)
    song_name = models.CharField(max_length=90,unique=True)
    slug_field = models.SlugField(max_length=90,unique=True)
    artists_name = models.CharField(max_length=90)
    song_img = models.ImageField(upload_to='testimg')
    description = models.TextField()
    rate_song = models.DecimalField(max_digits=5,decimal_places=2,default=3.0)
    mybest = models.BooleanField(default=True)
    categorry = models.ForeignKey(songmodel,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('det',args=[self.categorry.slug_field,self.slug_field],)

    def __str__(self):
        return '{}'.format(self.song_name)
