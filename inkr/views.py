from django.shortcuts import render
from .models import Pen, Ink

# Create your views here.
def matchr(request):
    pens = Pen.objects.all().order_by('name')
    inks = Ink.objects.all().order_by('name')
    return render(request, 'inkr/matchr.html', {'pens': pens, 'inks': inks})