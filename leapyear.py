import datetime

current_year=datetime.datetime.now().year
print('the current year is: ',current_year)
last_year=int(input("enter the last year:"))
print("the leap years from",current_year,"the",last_year,"is:")
for year in range(current_year,last_year+1):
 if year % 400==0 or (year % 4==0 and year % 100 !=0) :
    print(year)