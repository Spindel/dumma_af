from django.db import models

class User(models.Model):
    VOLONTEER= ( ('J', 'Söker Frivilligt'),
                 ('N', 'Tvingad av nya regler'),
               )
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)
    volonteer = models.CharField(max_length=1, choices=VOLONTEER)
    cv = models.TextField(max_length=10000)

    def __unicode__(self):
        return '<' + self.name + '> ' + self.email

class Corporation(models.Model):
    name = models.CharField(max_length=50, unique=True)
#    description = models.TextField()

    def __unicode__(self):
        return self.name
    # + ' ' + self.description

class Subscriber(models.Model):
    user = models.ForeignKey(User, unique=True)
    subscriptions = models.ManyToManyField(Corporation)



##
## http://stackoverflow.com/questions/2726476/django-multiple-choice-field-checkbox-select-multiple
#    class Meta:
#        unique_together = (("user", "corporation"))

class FormMail(models.Model):
    corporation = models.ForeignKey(Corporation)
    text = models.TextField()

    def __unicode__(self):
        return self.text

class Log(models.Model):
    date =  models.DateField(auto_now_add=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    status = models.CharField(max_length=50)
    form = models.ForeignKey(FormMail)

    def __unicode__(self):
        return self.date + ' <' + self.name + '> ' + self.email + ' ' + self.status
# Create your models here.
