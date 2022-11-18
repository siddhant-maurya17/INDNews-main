from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
# Create your models here.
class Category_Tag(models.Model):
  class Meta:
    verbose_name = "Category Tag"
  Category = models.CharField(max_length=20)
  Slug = models.SlugField()
  def __str__(self):
    return self.Category
    
class Author(models.Model):
  class Meta:
    verbose_name = "Author"
  Name = models.CharField(max_length=50)
  Image = models.ImageField(upload_to=f'Author/',help_text='SIZE 200X200',blank=True)
  def __str__(self):
    return self.Name

class News(models.Model):
  class Meta:
    verbose_name = "News"
    verbose_name_plural = 'News'
  Seo_Title = models.CharField(max_length=200,blank=True)
  Seo_Description = models.CharField(max_length=200,blank=True)

  Headline = models.TextField()
  Image = models.ImageField(upload_to='news/%Y/%M/%D',help_text='SIZE 1920X1272',blank=True)
  Content = RichTextUploadingField(blank=True)
  Tag = models.ForeignKey(Category_Tag,on_delete=models.CASCADE,blank=True)
  Author = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True)
  Date = models.DateTimeField()
  STATUS = [('Published','Published'),
            ('Draft','Draft')]
  Status = models.CharField(choices = STATUS,max_length=30 , default='Draft')

  Slug = models.SlugField(max_length=255, unique=True,default="")
  POSITION = [('Featured Big','Featured Big'),
              ('Featured Small','Featured Small'),
              ('Trending News','Trending News '),
              ('News Horizontal','News Horizontal'),
              ('News Verticle','News Verticle'),
              ('Most Popular','Most Popular'),]
  HomePage_Position = models.CharField(choices=POSITION,max_length=50 , default='News Verticle')

  def save(self, *args, **kwargs):
    if not self.Slug:
      self.Slug = slugify(self.Seo_Title)
    super(News, self).save(*args, **kwargs)
  def __str__(self):
    return self.Headline