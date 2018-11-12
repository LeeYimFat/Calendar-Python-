# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:01:19 2018
@author: Administrator
"""
def leap_year(year):
    
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False
    
def cal_month_day(year,month):
    days = 0
    
    if month == 2:
        days = 29 if leap_year(year) else 28
    else:    
        days = 31 if month in [1,3,5,7,8,10,12] else 30
    return days

def cal_weekday(year,month):
    totaldays = 0
    
    for i in range(1, year):
        totaldays += 366 if leap_year(i) else 365
    for i in range(1,month):
        totaldays += cal_month_day(year,i)
    return totaldays

def main():    
    count_week = 0
    year = int(input("年份： "))
    month = int(input("月份: "))
    print("\n")
    print("\t\t" + str(year) + "年" + str(month) + "月")
    print("\n")
    print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
    print("--------------------------------------------------------")   
    
    for i in range((cal_weekday(year,month)%7) + 1):
##两个个关键点： 1. 日历都是从周日开始 2. 公元元年一月一日，是周一。自己参详。 
        print("\t", end = '')
        count_week += 1
        
    for i in range(1, cal_month_day(year,month) + 1):       
        print (str(i) + "\t",  end='')
        count_week += 1   
        if count_week % 7 == 0:
            print("\n")
       
if __name__ == "__main__":
    main()

    












