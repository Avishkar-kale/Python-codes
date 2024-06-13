def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year=int(input("Enter year"))
month=int(input("enter month"))
days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
def days_in_month(year,month):
    if leap_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]

print(days_in_month(year,month))