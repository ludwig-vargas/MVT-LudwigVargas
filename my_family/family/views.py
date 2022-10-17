from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from family.models import Familiar

# Create your views here.
def create_familiar(request, name: str, last_name: str, numberphone: int, due_date: str):
    template = loader.get_template('template_familiar.html')
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    family = Familiar(name=name, last_name=last_name, numberphone=numberphone, birthday=due_date)
    family.save()
    
    context_dict = {'family': family}
    render = template.render(context_dict)
    return HttpResponse(render)

def familiar(request):
    familiar = Familiar.objects.all()
    
    context_dict = {'familiar': familiar}
    
    return render(
        request=request,
        context=context_dict,
        template_name='family/family_list.html',
    )    