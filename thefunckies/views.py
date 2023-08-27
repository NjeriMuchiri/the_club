from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    #converting month to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    context = {"year": year,
               "month": month,
               "month_number": month_number}
    return render(request, 'thefunckies/home.html', context)
