from django.db import models
from django.contrib import auth


class User(models.Model):
    VOLONTEER= ( ('J', 'Söker Frivilligt'),
                 ('N', 'Tvingad av nya regler'),
               )
    auth_user = models.ForeignKey(auth.models.User)
    name = models.CharField(max_length=250, null=False)
    volonteer = models.CharField(max_length=1, choices=VOLONTEER, blank=False,
                                 default='N', null=False)
    cv = models.TextField(max_length=10000, null=False)

    def __unicode__(self):
        return '<' + self.name + '> ' + self.email

class Corporation(models.Model):
    name = models.CharField(max_length=50, unique=True)
#    description = models.TextField()

    def __unicode__(self):
        return self.name
    # + ' ' + self.description


class Job(models.Model):
	name = models.CharField(max_length=200, unique=True)
	def  __unicode__(self):
		return self.name

class JobOpportunity(models.Model):
	corporation = models.ForeignKey(Corporation, unique=True)
	job = models.ManyToManyField(Job)

class Subscriber(models.Model):
	user = models.ForeignKey(User, unique=True)
	subscriptions = models.ManyToManyField(JobOpportunity)



##
## http://stackoverflow.com/questions/2726476/django-multiple-choice-field-checkbox-select-multiple
#    class Meta:
#        unique_together = (("user", "corporation"))

class FormMail(models.Model):
    corporation = models.ForeignKey(Corporation)
    job = models.ForeignKey(JobOpportunity)
    text = models.TextField()

    def __unicode__(self):
        return self.text

class Log(models.Model):
    date =  models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=50)
    form = models.ForeignKey(FormMail)

    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + ' ' + self.name + ' <' + self.email + '> ' + self.status
# Create your models here.
