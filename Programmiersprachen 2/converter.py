from _datetime import datetime
import time
import doctest

#Convert Input of Format YYYYMMDD Into Dates
def dateconvert(date_string):
    '''Main function which converts the given Date String into a datetime object. 
    This object then gets converted into 3 different Strings and one integer,
   which represent different expressions of dates in different calendars
    >>> print(dateconvert("20171224"))
    ('Sonntag, 24. Dezember 2017', 'Sunday, 24 December 2017', 'Sunday, 12/24/2017', 1514113200.0)
    >>> print(dateconvert("22010101"))
    Date out of Range
    >>> print(dateconvert("201705A1"))
    Invalid Input Format. Only Integers are allowed
    >>> print(dateconvert("2015A404"))
    Invalid Input Format. Only Integers are allowed
    >>> print(dateconvert("2015A404"))
    Invalid Input Format. Only Integers are allowed
    >>> print(dateconvert("123"))
    Input is too short or too long. Please use exactly 8 chars
    >>> print(dateconvert("007122016"))
    Input is too short or too long. Please use exactly 8 chars
    >>> print(dateconvert("18010101"))
    ('Donnerstag, 1. Januar 1801', 'Thursday, 1 January 1801', 'Thursday, 01/01/1801', 'There is no unix time pre 01.01.1970')
    >>> print(dateconvert("22001231"))
    ('Mittwoch, 31. Dezember 2200', 'Wednesday, 31 December 2200', 'Wednesday, 12/31/2200', 7289607600.0)
   '''
    date_string = str(date_string)
    if((len(date_string) < 8) or (len(date_string) > 8)):
        return "Input is too short or too long. Please use exactly 8 chars"
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
    '''Function to convert the integer which datetime.weekday returns to the according
    Term in the different calendars. The function gets the weekday from 0 to 6 as integer and the 
    calender format to convert to'''
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
    '''Function which uses a dictionary to convert the month integer
    to the according german names'''
    months_dict = {1: "Januar", 2: "Februar", 3: "März", 4: "April", 5: "Mai",
                  6: "Juni", 7: "Juli" , 8: "August", 9: "September",
                 10: "Oktober", 11: "November", 12: "Dezember"}
    return months_dict[m]

def get_german_date(converted_date):
    '''Function that gets a datetime object and converts it to a date String 
    according to the german calendar format and returns said String.'''
    date_str = ""
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"german"))
    day = str(converted_date.day)
    month = get_german_month(converted_date.month)
    year = str(converted_date.year)
    date_str = weekday_str + ", " + day + ". " + month + " " + year
    return date_str

def get_british_date(converted_date):
    '''Function that gets a datetime object and converts it to a date String 
    according to the british calendar format and returns said String'''
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"british"))
    year = str(converted_date.year)
    month = converted_date.strftime("%B")
    day = str(converted_date.day)

    date_str = weekday_str + ", " + day + " " + month + " " + year 
    return date_str

def get_american_date(converted_date):
    '''Function that gets a datetime object and converts it to a date String 
    according to the american calendar format and returns said String'''
    weekday = converted_date.weekday()
    weekday_str = (format_weekday(weekday,"american"))
    year = str(converted_date.year)
    month = str('%02d' % converted_date.month)
    day = str('%02d' % converted_date.day)
    date_str = weekday_str + ", " + month + "/" + day + "/" + year
    return date_str


def get_unix_date(converted_date):
    '''Function that gets a datetime object and converts it to Unix Time
    and returns said time as an Integer. Minimum Value for this Function is 01.01.1970.
    Will throw an OverflowError otherwise'''
    try:
        newtime = converted_date.replace(hour = 12, minute = 0)
        unix_time = time.mktime(newtime.timetuple())
    except OverflowError:
        return"There is no unix time pre 01.01.1970"
    return unix_time

def checkinput(date):
    '''Checks if the Input String is given in a valid format. If the Input is valid it returns
    the converted DateTime Object'''
    try:
        datetime.strptime(date, '%Y%m%d')

        return True
    except ValueError:
        print("Wrong Input Format. Use Integers in Format YYYYMMDD")
        return False

print(dateconvert("20171224"))
doctest.testmod()