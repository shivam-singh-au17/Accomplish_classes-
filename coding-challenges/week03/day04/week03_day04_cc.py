# a. Using break/continue on a nested loops of days and weeks (which you take as user input), skip out on the even days of all odd weeks.


wk = int(input("Enter week number: "))
dy = int(input("Enter day number: "))

for week in range(1, wk + 1):
    for day in range(1, dy + 1):
        if week % 2 == 1 and day % 2 == 0:
            continue
        print(" Week-", week, " Day-", day, end = "")
        if day%2 == 1:
            print(" odd")
        else:
            print(" even")



# b. Using break/continue on a nested loops of days and weeks (which you take as user input), encounter the scenario where we miss the first 2 classes ever and still complete the syllabus one week before the end.


wk = int(input("Enter week number: "))
dy = int(input("Enter day number: "))

for week in range(1, wk):
    for day in range(1, dy + 1):
        if week == 1 and day < 3:
            continue
        print(" Week-", week, " Day-", day, end = "")
        print(" ")
      

