from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Country
from django.shortcuts import redirect


def davlatlar(request):
    context = {
        'country': Country.objects.order_by('id')[::-1]
    }
    return render(request, 'home2.html', context)

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        c = Country(name=request.POST['name'], capital=request.POST['capital'])
        c.save()
        return redirect('davlatlar')
    return render(request, 'create.html')


def delete(request, id):
    Country.objects.filter(id=id).delete()
    return redirect("davlatlar")


def update(request, id):
    try:
        c = Country.objects.get(id=id)
    except Country.DoesNotExist:
        return redirect("davlatlar")
    if request.method == 'POST':
        c.name = request.POST["name"]
        c.capital = request.POST["capital"]
        c.save()
        return redirect("davlatlar")
    return render(request, 'create.html', {
        'c': c
    })


class CreateView(TemplateView):
    template_name = 'create.html'


