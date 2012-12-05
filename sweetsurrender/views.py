from django.http import HttpResponse
from django.template import Context, loader

def home(request):
    t = loader.get_template('home.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))

def product(request):
    t = loader.get_template('product.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('about.html')
    c = Context({'request':request})
    return HttpResponse(t.render(c))