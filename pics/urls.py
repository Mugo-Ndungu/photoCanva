from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/', views.pics_of_day, name='picsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',
        views.past_days_pics, name='pastPics'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^main/', views.page, name="location"),
    url(r'^location/', views.location, name="locations")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
