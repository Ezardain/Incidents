from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
    template = loader.get_template('project/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def manager(request, adminid):
    return HttpResponse("You're in admin view.")

def employee(request, empid):
    return HttpResponse("You're in employees view.")
