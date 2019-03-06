from django.shortcuts import render, HttpResponse, Http404, redirect
import datetime as dt
from .models import Pics

# Create your views here.


def welcome(request):
    return render('welcome.html')


def pics_of_day(request):
    date = dt.date.today()
    pics = Pics.get_pics()
    return render(request, 'all-pics/today-pics.html', {"date": date, "pics": pics})


def past_days_pics(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
        if date == dt.date.today():
            return redirect(pics_of_day)

    return render(request, 'all-pics/past-pics.html', {"date": date})


def search_results(request):

    if 'pics' in request.GET and request.GET["pics"]:
        category = request.GET.get("pics")
        searched_images = Pics.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any pics"
        return render(request, 'search.html', {"message": message})


def pics(request, image_id):
    try:
        pics = Pics.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "pics.html", {"pics": pics})


def location(request, location):
    locations = Pics.filter_by_location(location)
    return render(request, 'location.html', {"images": locations})


def page(request):
    return render(request, "main.html", {"title": location})
