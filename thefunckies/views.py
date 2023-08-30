from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

# Create your views here.
def home(request, year, month):
    
    #converting month to number
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    #craete calender
    the_calendar = HTMLCalendar().formatmonth(year, month_number)
    context = {"year": year,
               "month": month,
               "month_number": month_number,
               "the_calender": the_calendar}
    return render(request, 'thefunckies/home.html', context)
