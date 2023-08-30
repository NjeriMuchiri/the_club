from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request, year, month):
    #converting month to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #create calender
    the_calendar = HTMLCalendar().formatmonth(year, month_number)
    #Get the current year
    now = datetime.now()
    current_year = now.year
    context = {"year": year,
               "month": month,
               "month_number": month_number,
               "the_calendar": the_calendar,
               "current_year": current_year}
    return render(request, 'thefunckies/home.html', context)
