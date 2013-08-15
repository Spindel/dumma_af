# Create your views here.

from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello, world.  This is the index")

def log(request):
        return HttpResponse("This is the logs section")

def userLog(request, userid):
    return HttpResponse("This should return the log for user %s" % userid)


def emailLog(request, email):
    return HttpResponse("This should return the log for email %s" % email)
