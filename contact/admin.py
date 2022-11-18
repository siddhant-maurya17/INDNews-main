from django.contrib import admin
from .models import Messages
# Register your models here.
class MessagesAdmin(admin.ModelAdmin):
  list_display = ('name','email','subject','date','status')
  list_display_links = ('name','email')
  list_filter = ['status','date']
  fields= [('name','email'),'subject','message','date','status']

admin.site.register(Messages, MessagesAdmin)