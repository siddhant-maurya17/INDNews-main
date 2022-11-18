from django.contrib import admin
from .models import Category_Tag,Author,News
# Register your models here.
class Category_TagAdmin(admin.ModelAdmin):
  list_display = ('Category','Slug')
  list_display_links = ['Category']

admin.site.register(Category_Tag, Category_TagAdmin)

class AuthorAdmin(admin.ModelAdmin):
  list_display = ['Name']
  list_display_links = ['Name']

admin.site.register(Author, AuthorAdmin)

class NewsAdmin(admin.ModelAdmin):
  list_display = ('Headline','Tag','Author')
  list_display_links = ['Headline']
  list_filter = ['Tag','Status','Author','HomePage_Position','Date']
  fields = [('Seo_Title','Seo_Description'),('Headline','Image','Content','Tag','Author','Date'), 'Status','HomePage_Position','Slug']

admin.site.register(News, NewsAdmin)
