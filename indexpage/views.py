from django.http import HttpResponse
from django.shortcuts import render
from .models import Division, Profession, Worker
from .forms import DivisionCreateForm, ProfessionCreateForm, WorkerCreateForm

def index(request):
    return render(request, "index.html")

def divisions(request):
    divisions = Division.objects.all()
    return render(request,
                  'divisions\index.html',
                  {'divisions': divisions})

def division_create(request):
  if request.method == 'POST':
    form = DivisionCreateForm(request.POST)
    if form.is_valid():
      division = form.save()
      return render(request,
                    'divisions\created.html',
                    {'division': division})
  else:
    form = DivisionCreateForm()
    return render(request,
                  'divisions\create.html',{'form':form})

def professions(request):
    professions = Profession.objects.all()
    return render(request,
                  'professions\index.html',
                  {'professions': professions})

def profession_create(request):
  if request.method == 'POST':
    form = ProfessionCreateForm(request.POST)
    if form.is_valid():
        profession = form.save()
        return render(request,
                    'professions\created.html',
                    {'profession': profession})
  else:
    form = DivisionCreateForm()
    return render(request,
                  'divisions\create.html',{'form':form})


def workers(request):
    workers = Worker.objects.all()
    return render(request,
                  'workers\index.html',
                  {'workers': workers})

def worker_create(request):
  if request.method == 'POST':
    form = WorkerCreateForm(request.POST)
    if form.is_valid():
        worker = form.save()
        return render(request,
                    'workers\created.html',
                    {'str_worker': worker})
  else:
    form = WorkerCreateForm()
    return render(request,
                  'workers\create.html',{'form':form})




