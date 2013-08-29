# Create your views here.

from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from af.models import Corporation, Log, User

from django.shortcuts import render, get_object_or_404

from django.forms import ModelForm, RadioSelect

from django.contrib.auth.decorators import login_required

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'volonteer', 'cv')
        widgets = { 'volonteer': RadioSelect ,}

#class JobForm(ModelForm):
#    class Meta:
#        model = Job

def index(request):
    if request.user.is_authenticated():
        try:
            user = User.objects.get(auth_user=request.user)
            user_form = UserForm(instance=user)
        except ObjectDoesNotExist:
            user_form = UserForm()
    else:
        user_form = None
    corporation_list = Corporation.objects.all()
    context = {
        'corporation_list': corporation_list,
        'user_form': user_form,
    }
    return render(request, 'af/index.html', context)

@login_required
def log(request):
    user = User.objects.get(auth_user=request.user)
    user.email = user.auth_user.email
    last_log = Log.objects.order_by('-date')[:5]
    print(user)
    context = {'my_user': user,
               'my_logs': last_log,
              }
    return render(request, 'af/log.html', context)

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


class ApplyForm(ModelForm):
    class Meta:
        model = Corporation
        fields = ['name']



@login_required
def candidate(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auth_user = request.user
            instance.save()
            return HttpResponseRedirect('/log')
        else:
            return HttpResponseRedirect('/')

#     p = get_object_or_404(Corporation, pg=corporation)
#     try:
