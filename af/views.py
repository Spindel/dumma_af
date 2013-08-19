# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from af.models import Corporation, Log

from django.shortcuts import render


def index(request):
    corporation_list = Corporation.objects.all()
    context = {
        'corporation_list': corporation_list,
    }
    return render(request, 'af/index.html', context)

def log(request):
    last_log = Log.objects.order_by('-date')[:5]
    output = ', '.join([p.name for p in last_log])
    return HttpResponse(output)

def userLog(request, userid):
    return HttpResponse("This should return the log for user %s" % userid)


def emailLog(request, email):
    return HttpResponse("This should return the log for email %s" % email)

from django.http import Http404

def detail(request, logId):
    try:
        poll = Poll.objects.get(lg=log_id)
    except Log.DoesNotExist:
        raise Http404
    return render(request, 'af/detail.html', {'log':log})

def vote(request, corporation):
    return False

#     p = get_object_or_404(Corporation, pg=corporation)
#     try:
