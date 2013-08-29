from django.contrib import admin
from af.models import Corporation, Log, Subscriber, FormMail,User, Job, JobOpportunity

admin.site.register(User)
admin.site.register(Corporation)
admin.site.register(FormMail)
admin.site.register(Subscriber)
admin.site.register(Job)
admin.site.register(JobOpportunity)

class LogAdmin(admin.ModelAdmin):
    fields = ['email', 'name', 'status', 'form']
# don't hide required fields ;)
#    fieldsets = [
#        (None ,     {'fields': ['email', 'name', 'status']}),
#        ('Message', {'fields': ['form'],
#                     'classes': ['collapse'] }),
#    ]

admin.site.register(Log, LogAdmin)

