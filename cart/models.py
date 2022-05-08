from django.db import models
from idpass.models import song_details,songmodel
# Create your models here.
class cartlist(models.Model):
    cart_id = models.CharField(max_length=90,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    song_obj = models.ForeignKey(song_details,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    fav = models.BooleanField(default=True)
    def __str__(self):
        return self.song_obj

