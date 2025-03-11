import sys as s
"""
You work for the tech department of your city, and another government department
needs you to create a chatbot to help automate some of their common functions 
Dept of Motor Vehicles - Choice - only two options as of now
"""
prompts = ["If you need help about scheduling a license test, please type '1'", "If you need help registering a car, please type '2'", "If you need help with paying fees, please press 'N/A' ", "If you need help with rental cars, please press 'N/A'", "For exiting the program, please type 'exit'"]



print("Hello, I hope you are having a good day")

name = input(str("What is your name?\n"))
for i in range(len(prompts)):
    print(prompts[i])
print("Please put the number of which prompt you need")

while True:
    
    pHelp = input(str("What do you need help with, " + name + "?\n"))
    if pHelp == "1":
        print("What date would you like to schedule your test for(in M/D format | Ex: 1/23)?\n")
        try:
            print("What month?")
            month = input(int())
            print("What day?")
            day = input(int())
        finally:
            print("This date is avaliable!")
            print(name + ", your license test is scheduled for " + month + "/" + day)
#        except ValueError: This code did not work and I need 
 #           print("That's not a number!") to further debug it
    elif pHelp == "2":
        print("Have you gotten a vehicle inspection yet?(0 for no, 1 for yes)")
        q1 = input(str())
        if q1 == "1":
            print("Understood")
        elif q1 == "0":
            print("Please get a vehicle inspection before going any further")
        else:
            print("That's not a valid number!")
        print("Have you gotten a driver's registration yet?(0 for no, 1 for yes)")
        q2 = input(str())
        if q2 == "1":
            print("Understood")
        elif q2 == "0":
            print("Please get a vehicle registration before going any further")
        else:
            print("That's not a valid number!")
        print("Have you gotten a driver's license yet?(0 for no, 1 for yes)")
        q3 = input(str())
        if q3 == "1":
            print("Understood")
        elif q3 == "0":
            print("Please get a vehicle license before going any further")
        else:
            print("That's not a valid number!")
        print("Your car is able to get registered!")
    elif pHelp == "3":
        print()
    elif pHelp == "4":
        print()
    elif pHelp.lower() == "exit":
        s.exit(0)
    else:
        print("Sorry, that's not an option!")