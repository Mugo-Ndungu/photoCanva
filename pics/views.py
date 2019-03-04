from django.shortcuts import render, HttpResponse, Http404, redirect
import datetime as dt
from .models import Pics

# Create your views here.


def welcome(request):
    return render('welcome.html')


def pics_of_day(request):
    date = dt.date.today()
    pics = Pics.today_pics()
    return render(request, 'all-pics/today-pics.html', {"date": date,"pics":pics})




def past_days_pics(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
        if date == dt.date.today():
            return redirect(pics_of_day)

    return render(request, 'all-pics/past-pics.html', {"date": date})
