#create a calender using while loop
days = int(input("enter the number of days in a month : "))

day = 1
print("mon tue wed thu fri sat sun")

while day <= days:
    print(day,end="\t")
    if day % 7 == 0:
        print()
    day += 1