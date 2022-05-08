from django.shortcuts import render,redirect,get_object_or_404
from idpass.models import*
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_details(request):
    ct = cartlist.objects.get(cart_id=c_id(request))
    c_items = items.objects.filter(cart=ct,fav=True)
    return render(request,'cart.html',{
        'ci': c_items
    })

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request,product_id=None):
    song = song_details.objects.get(song_id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(song_obj=song,cart=ct)
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(song_obj=song,cart=ct)
        c_items.save()
        return redirect('cartDetails')

def cart_remove(request):
    pass

def cart_delete(request):
    pass