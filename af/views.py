# Create your views here.

from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from af.models import Corporation, Log

from django.shortcuts import render, get_object_or_404



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



#def detail(request, logId):
#    try:
#        poll = Poll.objects.get(lg=log_id)
#    except Log.DoesNotExist:
#        raise Http404
#    return render(request, 'af/detail.html', {'log':log})

from django.forms import ModelForm

class ApplyForm(ModelForm):
    class Meta:
        model = Corporation
        fields = ['name']

def candidate(request):
    if request.method == 'POST':
        form =  ApplyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/log')
        else:
            form = ApplyForm()
    return render(request, 'af/index.html', { 'form': form, })


#     p = get_object_or_404(Corporation, pg=corporation)
#     try:
