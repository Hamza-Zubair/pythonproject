from easygui import *
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
#This function returns the number of weeks of the Contract
def weekscalculator(inp):
    rawweeks=inp/7
    weeks = math.floor(rawweeks)
    return (weeks)
#This Function will create the list of weeks which will be used for assigning to team members
def makeweeklist(spoint, wlist): 
    if (spoint == wlist): 
        return spoint 
    else: 
        res = [] 
        while(spoint < wlist+1 ): 
            res.append(spoint) 
            spoint += 1
        return res 
#This Function use random function to assign number of weeks evenly to the tenants
def list_by_team(aList, size):
    """ return a list for a team """
    list_for_a_team = []
    for i in range(0, size):
        nbr = random.choice(aList)
        aList.remove(nbr)
        list_for_a_team.append(nbr)
    return list_for_a_team
#This Function will create a dictionary to save all the generated weeks to a dictionary
def MakeDictionary(Weeks):
    results = {}
    lenTeams = len(Teams) # i.e. 4
    lenWeeks = len(Weeks) # i.e. 52
    weeksPerTeam = int(lenWeeks / lenTeams)
    for i in range(0, lenTeams):
        key = Teams[i]
        value = list_by_team(Weeks, weeksPerTeam)
        results[key] = value
    return(results)
#This Function will create help to export weeks schedules with name of tenant
def excelwriter(listname,tenantname):
    row = 1
    column = 0
    worksheet.write(0, 0,"Cleaning Dates")
    worksheet.write(0, 1,"Name of Tenant")
    for item in listname.get(tenantname):
        worksheet.write(row, column, item)
        row += 1
    row = 1
    column = 1
    for item in listname.get(tenantname):
        worksheet.write(row, column,tenantname)
        row +=1
    workbook.close()
#This function creates week number to days (not a good function)
def daycreator(days,dic):
    for k,v in dic.items():
        day=[]
        for i in v:
            day.append(i*7)
        days.append(day)
    return(days)
#This is useful funtion which takes start date and list of days and gives back dates
def date_creator(startdate,weeklist):
    """Convert List of days to dates"""
    date=[]
    for weeklist in weeklist:
        for i in weeklist:
            day = startdate + datetime.timedelta(days=i)
            date.append(day.strftime('%d-%m-%Y'))
        dates.append(date)
    return (dates)

#My CODE BLOCK
try:
    userinput = enterbox("Enter the Starting Date of the Contract: ")
#    userinput = input("Enter the Starting Date of the Contract: ")
    date_str = userinput
    format_str = "%d/%m/%Y" 
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    userinput2 = enterbox("Enter the Ending Date of the Contract: ")
#    userinput2 = input("Enter the Ending Date of the Contract: ")
    date_str = userinput2
    format_str = "%d/%m/%Y"
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
except:
    print("Date not Valid, Program Terminating")
    exit()

a = enterbox ("Enter First Tenant Name: ")
a1 = enterbox ("Enter First Tenant's Email Address: ")
b = enterbox ("Enter Second Tenant Name: ")
b1 = enterbox ("Enter Second Tenant's Email Address: ")
c = enterbox ("Enter Third Tenant Name: ")
c1 = enterbox ("Enter Third Tenant's Email Address: ")
d = enterbox ("Enter Fourth Tenant Name: ")
d1 = enterbox ("Enter Fourth Tenant's Email Address: ")
Teams=[a,b,c,d]
email = [a1,b1,c1,d1]
startdate = datecon(userinput) # difference
enddate = datecon(userinput2)
diff = ((enddate)-(startdate)) #calculating the difference between dates
difference = str(diff)
clipdays = difference[:4] #clipping days from the result string
clipdaysfinal = int(clipdays)
wlist= (weekscalculator(clipdaysfinal))
print (wlist)#Calculating Weeks for the entered dates
FinalList= (makeweeklist(1,wlist)) #random generation of list to make dictionary of weeks per person
FinalDic = (MakeDictionary(FinalList)) #Make dictionary from random generated list

days=[]
dates=[]
daycreator(days,FinalDic)
date_creator(datetime_obj,days)

for key,i in zip(FinalDic.keys(),range(4)):
    FinalDic[key]=dates[i]

print ("Cleaning Week Schedule is as Following (Tenant Name : Weeks Numbers) " , FinalDic)
#Non Optimzed Code for Adding Excels for Tenant
workbook = xlsxwriter.Workbook('Tenant1.xlsx') 
worksheet = workbook.add_worksheet()
excelwriter(FinalDic,a)

workbook = xlsxwriter.Workbook('Tenant2.xlsx') 
worksheet = workbook.add_worksheet()
excelwriter(FinalDic,b)

workbook = xlsxwriter.Workbook('Tenant3.xlsx') 
worksheet = workbook.add_worksheet()
excelwriter(FinalDic,c)

workbook = xlsxwriter.Workbook('Tenant4.xlsx') 
worksheet = workbook.add_worksheet()
excelwriter(FinalDic,d)


#EMAIL GENERATION PART REMAINING

def create_notification(tenant_name,tenant_email):
    


