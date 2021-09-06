from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Articles,GeneralSetting,Menu
from django.conf import settings


# from django.shortcuts import render

# def hello(request):
#    return render(request, "template/index.html", {})

def index(request):

   artcs = Articles.objects.all().order_by('-id')
   mnus   = Menu.objects.all().order_by('id')
   setts  = GeneralSetting.objects.filter(id=1)[0]
   # return HttpResponse(setts)
   return render(request, 'index.html', {'artcs': artcs , 'mnus':mnus ,'setts':setts})

def show(request,articles_id):
   artcs = Articles.objects.filter(id=articles_id)[0]
   mnus   = Menu.objects.all().order_by('id')
   # return HttpResponse(artcs.text)
   return render(request, 'readmore.html', {'artc': artcs, 'mnus':mnus})

