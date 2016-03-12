# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
def index(request):
	from NoticeBoard.models import Notice
	from NoticeBoard.models import News
	notices = Notice.objects.all().exclude(expiry_date__lt=date.today())
	news = News.objects.all().exclude(expiry_date__lt=date.today())
	context = {'notices' : notices, 'nw' : news if news.count() else None}
	return render(request, 'NoticeBoard/index.html', context) 
def detail(request, title_req):
	from NoticeBoard.models import Notice
	notice = Notice.objects.filter(title=title_req)[0]
	context = {'notice' : notice,}
	return render(request, 'NoticeBoard/detail.html', context)
def list(request):
	from NoticeBoard.models import Notice
	recent_list = Notice.objects.all()
	context = {'recent_list': recent_list,}
	return render(request, 'NoticeBoard/list.html', context)
