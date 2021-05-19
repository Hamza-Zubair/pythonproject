from datetime import datetime

def datecon(userinput):
    date_str = userinput
    format_str = "%d/%m/%Y" # The format
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    return (datetime_obj.date())


try:
    userinput = input("Enter the Starting Date of the Contract: ")
    userinput2 = input("Enter the Ending Date of the Contract: ")
    datetime.strptime(userinput,'%d/%m/%Y')
    datetime.strptime(userinput2,'%d/%m/%Y')
except:
    print("Date not Valid, Program Terminating")
    exit()