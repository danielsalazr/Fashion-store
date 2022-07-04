from audioop import reverse
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Productos

# Create your views here.
def Index(request):
    return HttpResponse("Hola beba")

def createproduct(request):

    model = Productos
    template_name = "shop/createproduct.html"
    return render(request, template_name )





"""
class IndexView(generic.TemplateView):
    template_name= "shop/index.html"

    def get_queryset(self):
        #return de last five published questions
        #traerlas desde las mas recientes hasta las mas antiguas con el -pub_date
        #return Question.objects.order_by("-pub_date")[:5]
        return HttpResponse("Hola beba")
"""