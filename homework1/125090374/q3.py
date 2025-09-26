#get the input(hours and minutes in 24h format)
hour24 = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59):"))

if hour24 < 0 or hour24 > 23 or minute < 0 or minute > 59:
    print("Invalid time")

else:
    if hour24 > 12:#afternoon
        print("The time is: %02d:%02d PM" %(hour24 - 12, minute))

    elif hour24 == 12:#noon
        print("The time is: 12:%02d PM" %(minute))

    elif hour24 == 0:#midnight
        print("The time is: 12:%02d AM" %(minute))

    else:#morning
        print("The time is: %02d:%02d AM" %(hour24, minute))