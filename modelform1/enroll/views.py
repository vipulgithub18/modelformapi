from django.shortcuts import render
from .forms import StudentRegister
from django.http import HttpResponseRedirect,HttpResponse
from .models import Useradmin
# Create your views here.

def submited(request):
    return render(request,'enroll/success.html')

def ShowData(request):
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            # name = request.POST['name']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['pas']
            print(nm)
            print(em)
            print(pwd)
         
            return HttpResponseRedirect('/reg/success/')
            
    else:
        fm = StudentRegister()
    return render(request,'enroll/show.html',{'form':fm})
def About(request):
    return HttpResponse("<h2> this is MY about page</h2>")