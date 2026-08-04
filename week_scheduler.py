def scheduler():
    days_of_week = {
        "Sunday" : "",
        "Monday" : "",
        "Tuesday" : "",
        "Wednesday" : "",
        "Thursday" : "",
        "Friday" : "",
        "Saturday" : ""
    }

    print(f"Choose a day for plans:\n1.Sunday\n2.Monday\n3.Tuesday\n4.Wendsday\n5.Thursday\n6.Friday\n7.Saturday")

    choice = int(input("Enter a day: "))

    if choice == 1:
        plan = input("What are your plans for this day?")
        days_of_week["Sunday"] = plan
    elif choice == 2:
        plan = input("What are your plans for this day? ")
        days_of_week["Monday"] = plan
    elif choice == 3:
        plan = input("What are your plans for this day? ")
        days_of_week["Tuesday"] = plan
    elif choice == 4:
        plan = input("What are your plans for this day? ")
        days_of_week["Wednesday"] = plan
    elif choice == 5:
        plan = input("What are your plans for this day? ")
        days_of_week["Thursday"] = plan
    elif choice == 6:
        plan = input("What are your plans for this day? ")
        days_of_week["Friday"] = plan
    elif choice == 7:
        plan = input("What are your plans for this day? ")
        days_of_week["Saturday"] = plan
    else:
        print ("Error")
        return
    
    print(days_of_week)

scheduler()
        