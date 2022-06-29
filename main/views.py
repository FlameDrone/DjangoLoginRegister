from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Table, User
# Create your views here.

def index(request):
    table = Table.objects.get(id=1)
    print()
    name = ""
    if request.method == 'POST':
        name = request.POST.get('Username')
        if request.POST.get('Login'):
            for user in table.user_set.all():
                if request.POST.get('Username') == user.name:
                    if request.POST.get('Password') == user.password:
                        return HttpResponseRedirect("/home")
        elif request.POST.get('Register'):
            exists = False
            for user in table.user_set.all():
                if request.POST.get('Username') == user.name:
                    exists = True
            if not exists:
                if len(request.POST.get('Password')) > 7:
                    table.user_set.create(name = request.POST.get("Username"), password = request.POST.get('Password'))
                    return HttpResponseRedirect("/home")

    return render(request, 'main/RegisterLogin.html', {"username": name})

def home(request):
    return HttpResponse("<h1>Home</h1>") 