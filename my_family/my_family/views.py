from django.http import HttpResponse
from django.template import loader, Context

def hello_world(request):
    template = loader.get_template('template_hello.html')
    render = template.render()
    return HttpResponse(render)