from _datetime import datetime
from _datetime import date
import time
import converter

def main():
    strdate = input("Please input a Date in one of the following formats:" "YYYYMMDD or MM/DD/YYYY:")
    parse_result = parse_input(strdate)
    print("---------------------------------------------")
    if(not(parse_result) == "invalid"):
        date_tuple = converter.dateconvert(parse_result)
        for dates in date_tuple:
            print(dates)
    pass

def parse_input(dateinput):
    valid = False
    try:
        parsed_time = datetime.strptime(dateinput, '%Y%m%d')
        print("Format YYYYMMDD identified")
        print("Input was successfully parsed")
        return dateinput
    except ValueError:
        pass
 
    try:
        parsed_time = datetime.strptime(dateinput, '%m/%d/%Y')
        print("Format MM/DD/YYYY identified")
        print("Input was successfully parsed")
        parsed_string = parsed_time.strftime('%Y%m%d')
        return parsed_string
    except ValueError:
        pass
    print("Wrong Input Format. Use either YYYYMMDD or MM/DD/YYYY and only integers")
    return "invalid"

main()