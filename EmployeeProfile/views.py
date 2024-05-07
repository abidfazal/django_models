from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import NameForm 
from .models import Department
from django.contrib import messages

# Create your views here.

dep_name = [
        {'id' : 0, 'name' : 'Computer Science'},
        {'id' : 1, 'name' : 'Botony'},
        {'id' : 2, 'name' : 'Education'},
        {'id' : 3, 'name' : 'Socialogy'},
        {'id' : 4, 'name' :  'Economics'},
    ]

dep_details_list = [
        {'id' : 0, 'name' : 'Computer Science','location':'ls cafe',
         'chairperson':'Dr Rashid baloch'},
         {'id' : 1, 'name' : 'Botony','location':'first corner',
         'chairperson':'Dr Amjad rind'},
          {'id' : 2, 'name' : 'Education','location':'arong cafe',
         'chairperson':'madam Raseeda '},
        {'id' : 3, 'name' : 'Socialogy','location':'ls cafe',
         'chairperson':'Dr Qambar'},
        

]
def departments(request):
    deps = Department.objects.all()
    context = {
        'departments':deps
    }
    
    return render(request,'departments.html',context)

def dep_details(request,id):
    dep_tails = Department.objects.get(pk=id)
    context = {
        'dep_details': dep_tails
    }
    
    return render(request,'department_details.html',context)



def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        
        if form.is_valid():
            messages.success(request,'Form is submitted successfully')
            return redirect('thanks')
        
    else:
        form = NameForm()
        
    return render(request, 'login.html', {'form': form})