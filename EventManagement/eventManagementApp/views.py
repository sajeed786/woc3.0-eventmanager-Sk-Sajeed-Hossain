from datetime import date, datetime
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from eventManagementApp.models import Event

# Create your views here.
def homepage(request):
    template = loader.get_template('eventManagementApp/index.html')
    context = {
        'data': 'Welcome, here!!'
    }
    return HttpResponse(template.render(context, request))

def eventRegisterPage(request):
    if(request.method == 'POST'):
        event = Event()
        form_data = request.POST
        event.event_name = form_data.get('event_name')
        event.event_description = form_data.get('event_description')
        event.venue = form_data.get('venue')
        event.event_poster_link = form_data.get('poster_url')
        event.start_date = form_data.get('start_date')
        event.start_time = form_data.get('start_time')
        event.end_date = form_data.get('end_date')
        event.end_time = form_data.get('end_time')
        event.registration_end_date = form_data.get('reg_end_date')
        event.registration_end_time = form_data.get('reg_end_time')
        event.host_emailid = form_data.get('host_emailid')

        try:
            event.save()
            messages.success(request, 'Event registered successfully with us!', extra_tags='alert')

        except:
            messages.error(request, 'An unexpected error occured while saving the data into database', extra_tags='alert')
            
        eventDetails = {
                'eventName': event.event_name,
                'eventId': event.pk
            }
        html_content = loader.get_template('eventManagementApp/mail.html').render(eventDetails)
        send_mail(
                'Event Registration - Successful',
                'Success',
                settings.EMAIL_HOST_USER,
                [event.host_emailid],
                fail_silently=False, 
                html_message=html_content
        )

        messages.success(request, 'Details have been sent to your email id', extra_tags='alert')
        
    template = loader.get_template('eventManagementApp/eventRegistration.html')
    context = {}
    return HttpResponse(template.render(context, request))

def participantRegisterPage(request):
    template = loader.get_template('eventManagementApp/participantRegistration.html')
    context = {
        'activeEvents': Event.objects.filter(
                                            Q(registration_end_date__gt = date.today().strftime("%Y-%m-%d")) | ( Q(registration_end_date__exact = date.today().strftime("%Y-%m-%d")) & Q(registration_end_time__gt = datetime.now().strftime("%H:%M")) )
        )
    }
    return HttpResponse(template.render(context, request))
