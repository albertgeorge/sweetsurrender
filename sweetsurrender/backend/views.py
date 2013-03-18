from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

def load_login_page(request):
    return render_to_response('admin/login.html', context_instance=RequestContext(request))

def login(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #user = authenticate(username=username, password=password)
        
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                state = "You're successfully logged in!"
#            else:
#                state = "Your account is not active, please contact the site admin."
#        else:
#            state = "Your username and/or password were incorrect."

    return render_to_response('adminhome.html')

def admin_home(request):
    return render_to_response('admin/adminhome.html', context_instance=RequestContext(request))