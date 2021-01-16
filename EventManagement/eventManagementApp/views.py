from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homepage(request):
    template = loader.get_template('eventManagementApp/index.html')
    context = {
        'data': 'Welcome, here!!'
    }
    return HttpResponse(template.render(context, request))