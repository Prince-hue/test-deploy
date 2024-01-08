from django.shortcuts import render
from django.http import HttpResponse
from .models import deploy

from .models import deploy
from .forms import deployforms
from django.shortcuts import redirect


# Create your views here.
def index(request):
    deploy_app = deploy.objects.all()
    return render(request, "index.html", {'deploy_app': deploy_app}) 

#deploy experiment


def deployy(request):
    deploy_app = deploy.objects.all()
    if request.method == 'POST':
        form = deployforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deployy')
    else:
        form = deployforms()
    dic = {
        'deploy_app': deploy_app,
        'form': form,
    }
    return render(request, 'index.html', dic)