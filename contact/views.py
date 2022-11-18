from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Messages
from django.db.models import Q
from news.models import News,Category_Tag
# Create your views here.
def contact(request):
    trending_news = News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Trending News') & Q(Status__iexact= 'Published'))
    tags = Category_Tag.objects.all()
    Most_Popular= News.objects.order_by('-Date').filter(Q(HomePage_Position__iexact = 'Most Popular') & Q(Status__iexact= 'Published'))
    context ={
    'trending_news':trending_news[:7],
    'ft_tag': tags[:7],
    'Most_Viewed':Most_Popular[:3],
    }
    if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      subject  = request.POST['subject']
      message = request.POST['message']

      message = Messages(name = name, email=email,subject=subject ,message = message)
      message.save()
      messages.success(request, 'Hurray! We Have Received Your Message.Thanks For Contacting')
      return redirect('contact')

    else:
      return render(request, 'pages/Contact.html',context)