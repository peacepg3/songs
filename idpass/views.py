# # from django.forms import ModelForm
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
#
# from . models import pgattribute
# from .form1 import pgattrifrom
# import calendar
# from calendar import HTMLCalendar
# from . addform import modeform
# # Create your views here.
# def idapp(request):
#
#     # obj.attri1 = 'peace'
#     # obj.attri2 = 'science'
#     # obj.attri3 = 'magic'
#     # obj.attri9 = 3
#     # obj1 = 'peace'
#     # obj2 = 'science'
#     # obj3 = 'magic'
#     # obj = [obj1,obj2,obj3]
#     obj = pgattribute.objects.all()
#     return render(request,'id.html',{'object':obj})
#
# def details(request,ids):
#     obj1 = pgattribute.objects.get(id=ids)
#     return render(request,'details.html',{'des':obj1})
#
# def delte(request,ide):
#     if request.method == 'POST':
#         delt = pgattribute.objects.get(id=ide)
#         delt.delete()
#         return redirect('/')
#     return render(request,'deletee.html')
#
# #
# # def add(request):
# #
# #     if request.method == 'POST':
# #         objv = request.POST.get('attri1')
# #         obji = request.POST.get('attri2')
# #         objs = request.POST.get('attri3')
# #         objh = request.POST.get('attri9')
# #         objn = pgattribute(attri1=objv,attri2=obji,attri3=objs,attri9=objh)
# #         objn.save()
# #         print('yes its saved')
# #     return render(request,'addsomething.html')
#
# def updateatt(request,ide):
#     pg = pgattribute.objects.get(id=ide)
#     frm = modeform(request.POST or None,request.FILES,instance=pg)
#     if frm.is_valid():
#         frm.save()
#         return redirect('/')
#     return render(request,'add.html', {'frm':frm})
#
# def update(request):
#
#     if request.method =='POST':
#         formone = pgattrifrom(request.POST)
#         if formone.is_valid():
#             formone.save()
#             return HttpResponse('work submitted')
#         # else:
#         #     return redirect('edit.html')
#     formone = pgattrifrom
#     return render(request,'edit.html',{'formone':formone})
#
# def calender(request,year,month):
#     name = 'pg3'
#     # month = month.capitalize()
#     month = month.capitalize()
#     if month in list(calendar.month_name):   # THIS THING I JUST DO MYSELF VOHH GREAT.
#         month_number = list(calendar.month_name).index(month)
#     else:
#         return HttpResponse('check spelling')
#     cal = HTMLCalendar().formatmonth(theyear=year,themonth=month_number)
#     month_number = int(month_number)
#     return render(request,'calender.html',{
#         'name': name,
#         'year': year,
#         'month': month,
#         'month_number': month_number,
#         'cal' : cal,
#     })
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.db.models import Q
from .models import song_details, songmodel
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist


def songview(request, slg_variable=None):

    if slg_variable!=None:

        pge = get_object_or_404(songmodel,slug_field=slg_variable)
        sd1 = song_details.objects.filter(categorry=pge,mybest=True)
    else:
        sd1 = song_details.objects.filter(mybest=True)
    #sd = song_details.objects.all()
    p = Paginator(object_list=sd1,per_page=3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        page_obj = p.page(page)
    except(EmptyPage,InvalidPage):
        page_obj = p.page(p.num_pages)

    sm = songmodel.objects.all()
    return render(request, 'songs_home2.html', {'obj': sd1 ,
                                                'sm': sm,
                                                'pg': page_obj })
def prod_detail(request,c_slug,prod_variable):
    prod = song_details.objects.get(categorry__slug_field=c_slug,slug_field=prod_variable)
    return render(request,'details_music.html',{'pd':prod})
# def search_song(request):
#     product= None
#     quary = None
#     if 'q' in request.GET:
#         quary = request.GET.get('q')
#         product = song_details.objects.all().filter(Q(name__contains= quary)|Q(description__contains=quary))
#
#     return render(request,'search.html',{'qr':quary,'pr':product})
def search_song(request):
    if 'search' in  request.GET:
        searched = request.GET['search']
        results = song_details.objects.all().filter(Q(description__contains=searched)| Q(song_name__contains=searched)| Q(artists_name__contains=searched))
        return render(request,'search.html',
        {'srh':searched,
         'result':results})
    else:
        return render(request,'songs_home2.html')
