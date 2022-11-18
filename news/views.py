from django.shortcuts import render,HttpResponse
from .models import Category_Tag,News
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
  tags = Category_Tag.objects.all()
  featured_news_big = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Featured Big') & Q(Status__iexact= 'Published'))
  featured_news_small = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Featured Small') & Q(Status__iexact= 'Published'))
  trending_news = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Trending News') & Q(Status__iexact= 'Published'))
  News_Horizontal = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'News Horizontal') & Q(Status__iexact= 'Published'))
  News_Vertical= News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'News Verticle') & Q(Status__iexact= 'Published'))
  Most_Popular= News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Most Popular') & Q(Status__iexact= 'Published'))

  paginator = Paginator(News_Vertical, 6)
  page = request.GET.get('page')
  paged_news = paginator.get_page(page)

  context = {
    'tags' : tags,
    'ft_tag': tags[:7],
    'featured_news_big':featured_news_big[:1],
    'featured_news_small':featured_news_small[:4],
    'trending_news':trending_news[:7],
    'News_Horizontal':News_Horizontal[:7],
    'News_Verical':paged_news,
    'Most_Popular':Most_Popular[:4],
    'Most_Viewed':Most_Popular[:3],

  }
  return render(request, "pages/index.html",context)

def category(request,pk):
  Category = News.objects.order_by('-Date').filter(Tag__Category__icontains = pk)
  tags = Category_Tag.objects.all()
  category_tag = Category_Tag.objects.get(Category__icontains=pk)
  Most_Popular= News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Most Popular') & Q(Status__iexact= 'Published'))
  trending_news = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Trending News') & Q(Status__iexact= 'Published'))

  paginator = Paginator(Category, 5)
  page = request.GET.get('page')
  paged_news = paginator.get_page(page)
  
  context ={
    'category':paged_news,
    'tags':tags,
    'ft_tag': tags[:7],
    'Most_Popular':Most_Popular[:4],
    'trending_news':trending_news[:7],
    'category_tag':category_tag,
    'Most_Viewed':Most_Popular[:3],
  }
  return render(request, "pages/category-detail.html",context)

def news(request,sk):
  Post = News.objects.get(Slug=sk)
  trending_news = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Trending News') & Q(Status__iexact= 'Published'))
  tags = Category_Tag.objects.all()
  Most_Popular= News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Most Popular') & Q(Status__iexact= 'Published'))
  context ={
    'News':Post,
    'trending_news':trending_news[:7],
    'tags' : tags,
    'Most_Popular':Most_Popular[:4],
    'ft_tag': tags[:7],
    'Most_Viewed':Most_Popular[:3],
  }
  return render(request, "pages/detail-page.html",context)