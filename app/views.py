from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def student_reg(request):
    
    SFO = StudentForm()
    D = {'SFO' : SFO}
    
    if request.method == 'POST':
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            
            return HttpResponse('Data is Submitted')
        
        else:
            return HttpResponse('Data is not Valid')
    
    return render(request, 'student_reg.html', D)
