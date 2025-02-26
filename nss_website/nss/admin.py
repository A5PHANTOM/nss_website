from django.contrib import admin
from .models import Program, ProgramPhoto, MoreProgramPhoto,UpcomingEvent

admin.site.register(Program)
admin.site.register(ProgramPhoto)
admin.site.register(MoreProgramPhoto)
admin.site.register(UpcomingEvent)