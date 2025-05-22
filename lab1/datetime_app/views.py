from django.shortcuts import render
import datetime
# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    four_hours_ahead = now + datetime.timedelta(hours=4)
    four_hours_before = now - datetime.timedelta(hours=4)

    context = {
        "current_time": now,
        "four_hours_ahead": four_hours_ahead,
        "four_hours_before": four_hours_before,
    }

    return render(request, "datetime_app/current_datetime.html", context)
