from _datetime import datetime
from _datetime import date
import time

#Convert Input of Format YYYYMMDD Into Dates
def dateconvert(date_string):
    if((len(date_string) < 8) or (len(date_string) > 8)):
        return "Input is too short or too long. Plese use exactly 8 chars"
    date_string = str(date_string)
    if(not date_string.isnumeric()):
        return "Invalid Input Format. Only Integers are allowed"
    if(checkinput(date_string)):
        dateinput = datetime.strptime(date_string, "%Y%m%d")
        if(datetime(1801,1,1) <= dateinput <= datetime(2200,12,31)):
            german_date = get_german_date(dateinput)
            british_date = get_british_date(dateinput)
            american_date = get_american_date(dateinput)
            unix_date = get_unix_date(dateinput)
        else: 
            return "Date out of Range"    
        return (german_date, british_date, american_date, unix_date)
    else: return "Invalid Input Format. Use YYYYMMDD"


def format_weekday(weekday, dateformat):
    weekday_str = ""
    if(weekday == 0):
        if(dateformat == "german"):
            weekday_str = "Montag"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Montag"
    elif(weekday == 1):
        if(dateformat == "german"):
            weekday_str = "Dienstag"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Tuesday"
    elif(weekday == 2):
        if(dateformat == "german"):
            weekday_str = "Mittwoch"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Wednesday"
    elif(weekday == 3):
        if(dateformat == "german"):
            weekday_str = "Donnerstag"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Thursday"
    elif(weekday == 4):
        if(dateformat == "german"):
            weekday_str = "Freitag"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Friday"
    elif(weekday == 5):
        if(dateformat == "german"):
            weekday_str = "Sonnabend"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Saturday"
    elif(weekday == 6):
        if(dateformat == "german"):
            weekday_str = "Sonntag"
        elif((dateformat == "british") or (dateformat == "american")):
            weekday_str = "Sunday"
    return weekday_str

def get_german_month(m):
    months_dict = {1: "Januar", 2: "Februar", 3: "März", 4: "April", 5: "Mai",
                  6: "Juni", 7: "Juli" , 8: "August", 9: "September",
                 10: "Oktober", 11: "November", 12: "Dezember"}
    return months_dict[m]

def get_german_date(converted_date):
    date_str = ""
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"german"))
    day = str(converted_date.day)
    month = get_german_month(converted_date.month)
    year = str(converted_date.year)
    date_str = weekday_str + ", " + day + ". " + month + " " + year
    return date_str

def get_british_date(converted_date):
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"british"))
    year = str(converted_date.year)
    month = converted_date.strftime("%B")
    day = str(converted_date.day)

    date_str = weekday_str + ", " + day + " " + month + " " + year 
    return date_str

def get_american_date(converted_date):
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"american"))
    year = str(converted_date.year)
    month = str('%02d' % converted_date.month)
    day = str('%02d' % converted_date.day)
    date_str = weekday_str + ", " + month + "/" + day + "/" + year
    return date_str


def get_unix_date(converted_date):
    newtime = converted_date.replace(hour = 12, minute = 0)
    unix_time = time.mktime(newtime.timetuple())
    return unix_time

def checkinput(date):
    try:
        datetime.strptime(date, '%Y%m%d')

        return True
    except ValueError:
        print("Wrong Input Format. Use Integers in Format YYYYMMDD")
        return False

