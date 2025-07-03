year=int(input("ENTER THE YEAR : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"IS Leap year")
        else :
            print(year,"IS not Leap year")
    else :
        print(year,"IS  Leap year")
else:
    print(year,"IS not Leap year")

    