from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.pics_of_day,name='picsToday'),
    url('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pics,name='pastPics')
]