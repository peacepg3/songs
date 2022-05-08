from django.shortcuts import render, redirect
from .models import todomodel
from .updateform import updform
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class listview(generic.ListView):
    model = todomodel
    template_name = 'todotask.html'
    context_object_name = 'obj'

class detailview(generic.DetailView):
    model = todomodel
    template_name = 'tdobase.html'


class updateview(generic.UpdateView):
    model = todomodel
    template_name = 'update.html'
    context_object_name = 'save'
    fields = ('work','time','date')
    def get_success_url(self):
        return reverse_lazy('details',kwargs={'pk':self.object.id})
class deleteview(generic.DetailView):
    model = todomodel
    template_name = 'delete.html'
    success_url = reverse_lazy('generic')

# def goto(request):
#
#     return render(request,'upd.html')

def todo(request):
    obj1 = todomodel.objects.all()

    if request.method == 'POST':
        work = request.POST.get('work')
        time = request.POST.get('time')
        date = request.POST.get('date')
        obj = todomodel(work=work, time=time,date=date)
        obj.save()
    return render(request, 'todotask.html', {'obj': obj1})

def delt(request,dltid):
    dlt = todomodel.objects.get(id=dltid)
    if request.method == 'POST':
        dlt.delete()
        return redirect('/')
    return render(request, 'Delete.html')

def update(request,updateid):
    upd = todomodel.objects.get(id=updateid)
    frm = updform(request.POST or None, instance=upd)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'upd.html',{'form':frm})

