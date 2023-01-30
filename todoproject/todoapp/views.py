from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import Todoform
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView,DeleteView
# Create your views here.

class taskview(ListView):
    model=Task
    template_name ='home.html'
    context_object_name = 'task1'

class taskdetail(DetailView):
    model=Task
    template_name ='details.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

class taskupdate(UpdateView):
    model=Task
    template_name ='update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('newdetail' ,kwargs={'pk':self.object.id})

class taskdelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('newfun')



def value(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        if priority=="":
             priority=None
        date = request.POST.get('date','')

        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'task1':task1})

# def details(request):
#
#     return render(request,'details.html')

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form,'task':task})