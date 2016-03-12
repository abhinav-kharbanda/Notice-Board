from django.contrib import admin
from NoticeBoard.models import Notice
from NoticeBoard.models import News
class NoticeAdmin(admin.ModelAdmin):
	fields = ('title', 'sub_title', 'display_title', 'publish_date', 'expiry_date', 'content', 'image', 'sign_image', 'video', 'display_video') #,'author' ,'priority') 
	list_display = ('title', 'publish_date', 'expiry_date', 'is_expired')	#,'author')
	list_filter = ['publish_date'] #,'author', 'priority')
	search_fields = ['title']
class NewsAdmin(admin.ModelAdmin):
	fields = ('title', 'publish_date', 'expiry_date')
	list_display = ('title', 'publish_date', 'expiry_date', 'is_expired')	
	list_filter = ['publish_date']
	search_fields = ['title']
admin.site.register(Notice, NoticeAdmin)
admin.site.register(News, NewsAdmin)
