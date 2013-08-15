# Create your views here.

from django.http import HttpResponse

from af.models import Log

def index(request):
        return HttpResponse("This is the index function")

def log(request):
    last_log = Log.objects.order_by('-date')[:5]
    output = ', '.join([p.name for p in last_log])
    return HttpResponse(output)

def userLog(request, userid):
    return HttpResponse("This should return the log for user %s" % userid)


def emailLog(request, email):
    return HttpResponse("This should return the log for email %s" % email)
