from datetime import datetime, date, timedelta
import math

def ConvertFloat_ValueInto_Time(value):

    result = '{0:02.0f}:{1:02.0f}'.format(*divmod(value * 60, 60))

    return result


def ConvertMinutes_Into_Hours(value):

    result = '{:02d}:{:02d}'.format(*divmod(value, 60))

    return result


def Diffecnce_Between_TwoDays(start_date, end_date):

    # This functions works only for the date format of (year, month, date), eg: (2000, 03, 01)

    start_date = date(start_date)
    end_date = date(end_date)

    delta = end_date - start_date

    result = delta.days + 1

    return result


def Get_CurrentTime():

    now = datetime.now()

    current_time = now.strftime("%I:%M:%S")

    # current_time = now.strftime("%H:%M:%S")     For 24 hour format

    # current_time = datetime.now().strftime("%I:%M:%S")   We also can use like this

    return current_time


def Get_Month_Day_Week_From_A_Date(the_date):

    # The suitable date format '2010-01-31'

    date_conversion = datetime.strptime(the_date, "%Y-%m-%d")

    #  The Parameter "the_date" must be a string

    print(date_conversion.strftime("%B"))  # Month
    print(date_conversion.strftime("%A"))  # Day

    print(datetime.date(2010, 6, 16).isocalendar().week)  # Week

    # or 

    print(date(2010, 6, 16).isocalendar().week)  # Week


def GetThe_Previous_Date_OfA_Date(sdate):

    # The suitable date format '2010-01-31'

    closing_date = datetime.strptime(sdate, "%Y-%m-%d").date() - timedelta(1)

    sdate = datetime.today().date()

    a = sdate  - timedelta(1)
    b = str(a)

    closing_date = datetime.strptime(b, "%Y-%m-%d").date()
    print(closing_date)


def LoopThrough_DateRange(start_date, end_date):

    # This functions works only for the date format of (year, month, date), eg: (2000, 03, 01)

    start_date = date(start_date)
    end_date = date(end_date)
    delta = timedelta(days=1)

    while start_date <= end_date:
        print(start_date.strftime("%Y-%m-%d"))
        start_date += delta


    # Alter Method

    """

    sdate = date(start_date)   # start date
    edate = date(end_date)   # end date

    delta = edate - sdate       # as timedelta

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        print(day)
    
    """


def LoopThrough_DateRange_ForDjango(start_date, end_date):

    # The suitable date format '2010-01-31'

    a = start_date.split("-")

    b = end_date.split("-")

    d1 = date(int(a[0]), int(a[1]), int(a[2]))

    d2 = date(int(b[0]), int(b[1]), int(b[2]))

    delta = timedelta(days=1)

    while d1 <= d2:
        d1 += delta
        print(d1.strftime("%Y-%m-%d"))


def Minutes_To_Day_Hours_Minutes_Format(total_minutes):

    days = math.floor(total_minutes / (24*60))
    leftover_minutes = total_minutes % (24*60)
    hours = math.floor(leftover_minutes / 60)

    mins = total_minutes - (days*1440) - (hours*60)
    result = f"{days} days: {hours} hrs: {mins} mins"
    return result


def Convert12_HourFormat_To_24Hour_Format(time):

    # Supported time format "08:01:00 AM" or "06:00:00 PM"

    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
        
    elif time[-2:] == "AM":
        return time[:-2]

    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
        
    else:
        
        return str(int(time[:2]) + 12) + time[2:8]
    