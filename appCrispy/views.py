from django.shortcuts import render
from appCrispy.forms import EngineerForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from appCrispy.models import Engineer
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

#-----------------------------FRONTEND-------------------------------------|
#HOME
def home (request):
  return render(request, 'home.html')

#ENGINEER REGISTRATION
def register(request):
  if request.method == 'POST':
    form = EngineerForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form Submitted Successfully')
        return HttpResponseRedirect('register')
    else:
      return render(request, 'register.html' , {'form': form })
  else: 
    form = EngineerForm()
    return render(request, 'register.html' , {'form': form })


#----------------------------- BACKEND -------------------------------------|

@login_required (login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
  context = {
    'data_read':Engineer.objects.all()
  }
  return render(request, 'backend.html', context)


@login_required (login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def engineer(request, id):
  engineer = Engineer.objects.get(id=id)
  # form = EngineerForm(instance=data)
  return render(request, 'engineer.html', {'engineer': engineer})

