# Movie Ticket
ANS = "Yes"
Pnp = 0
Enp = 0
Pst = 0
Est = 0
TPamt = 0
TEamt = 0
while ANS.lower() == "yes":
    print("Menu: \nEnter 'P' for Premium Seat \nEnter 'E' for Executive Seat")
    ch = input("Enter your choice(Premium/Executive): ")
    if ch.lower() == 'p' or ch.lower() == 'premium':
        print(f"Available seats {100 - Pst}")
        np = int(input("Enter Number of People: "))
        Pnp = Pnp + np
        if Pnp <= 100:
            Pst = Pst + np
            Pamt = np * 300
            TPamt = TPamt + Pamt
            print(f"Number of Seats booked = {np}")
            print(f"Total amount to be paid = {Pamt}")
        else:
            print("Houseful")
    elif ch.lower() == 'e' or ch.lower() == "exclusive":
        print(f"Available seats {50 - Est}")
        np = int(input("Enter Number of People: "))
        Enp = Enp + np
        if Enp <= 50:
            Est = Est + np
            Eamt = np * 500
            TEamt = TEamt + Eamt
            print(f"Number of Seats booked = {np}")
            print(f"Total amount to be paid = {Eamt}") 
        else:
            print("Houseful")
    else:
        print("Invalid Choice")
    ANS = input("Do you want to continue: ")
while ANS.lower() == "no":
    print(f"Total Number of Premium Seats booked = {Pst}\nTotal amount of money earned from selling Premium Seats = {TPamt}"
      f"\nTotal Number of Executive Seats booked = {Est}\nTotal amount of money earned from selling Executive Seats = "
      f"{TEamt}\nTotal seats sold = {Pst+Est}\nTotal Collection = {TPamt+TEamt} \n\nThank you for using this program")
    break
else:
    print("Invalid Answer")

'''OUTPUT:

Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): P
Available seats 100
Enter Number of People: 99
Number of Seats booked = 99
Total amount to be paid = 29700
Do you want to continue: yes
Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): P
Available seats 1
Enter Number of People: 1
Number of Seats booked = 1
Total amount to be paid = 300
Do you want to continue: yes
Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): p
Available seats 0
Enter Number of People: 1
Houseful
Do you want to continue: yes
Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): E
Available seats 50
Enter Number of People: 49
Number of Seats booked = 49
Total amount to be paid = 24500
Do you want to continue: yes
Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): E
Available seats 1
Enter Number of People: 1
Number of Seats booked = 1
Total amount to be paid = 500
Do you want to continue: yes
Menu: 
Enter 'P' for Premium Seat 
Enter 'E' for Executive Seat
Enter your choice(Premium/Executive): E
Available seats 0
Enter Number of People: 1
Houseful
Do you want to continue: no
Total Number of Premium Seats booked = 100
Total amount of money earned from selling Premium Seats = 30000
Total Number of Executive Seats booked = 50
Total amount of money earned from selling Executive Seats = 25000
Total seats sold = 150
Total Collection = 55000

Thank you for using this program

'''

    
    
