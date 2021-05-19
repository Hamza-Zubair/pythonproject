import datetime
import time
import math
import random
import xlsxwriter
#This Function will Convert user input of Dates
def datecon(userinput):
    date_str = userinput
    format_str = "%d/%m/%Y" # The format
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    return (datetime_obj.date())

try:
    userinput = input("Enter the Starting Date of the Contract: ")
    date_str = userinput
    format_str = "%d/%m/%Y" 
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    userinput2 = input("Enter the Ending Date of the Contract: ")
    date_str = userinput2
    format_str = "%d/%m/%Y"
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
except:
    print("Date not Valid, Program Terminating")
    exit()


startdate = datecon(userinput) # difference
enddate = datecon(userinput2)
diff = ((enddate)-(startdate)) #calculating the difference between dates
print (diff)
difference = str(diff)
print (difference)


clipdays = difference.split(" ")[0] #clipping days from the result string
print (clipdays)
#clipdaysfinal = int(clipdays)
#print (clipdaysfinal)
