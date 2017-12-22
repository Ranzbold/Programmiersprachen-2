from _datetime import datetime
from _datetime import date
import time
import converter

def main():
    '''Main function which handles user input. The function passes its
    input to the parse_input function, which returns a String according
    to the validity of the input. If the Input is valid the function passes
    the valid input to the dateconvert function of the converter module'''
    strdate = input("Please input a Date in one of the following formats:" "YYYYMMDD or MM/DD/YYYY:")
    parse_result = parse_input(strdate)
    print("---------------------------------------------")
    if(not(parse_result) == "invalid"):
        date_tuple = converter.dateconvert(parse_result)
        for dates in date_tuple:
            print(dates)
    pass

def parse_input(dateinput):
    ''' Function that checks the validity of the given Date String
    The String Formats YYYYMMDD and MM/DD/YYYY are supported'''
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