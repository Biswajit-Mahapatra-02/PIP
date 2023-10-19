def isLeap(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else: return False
def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    assert month <= 12
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print("Number of days is 31")
    elif month == 2:
        if isLeap(year):
            print("Number of days is 29")
        else:
            print("Number of days is 28")
    else:
        print("Number of days is 30")
main()
