import sys
prompts = ["PLACEHOLDER", "PLACEHOLDEr", "PLACEHOLDer", "EXIT"]



print("Hello, I hope you are having a good day")

name = input(str("What is your name?\n"))

print("What is your age?")
age = input(int())

while True:
    for i in range(len(prompts)):
        print(prompts[i])
    pHelp = input(str("What do you need help with?\n"))
    if pHelp == "PLACEHOLDER":
        print("PLACEHOLDER")
    elif pHelp == "EXIT":
        print("Have a good day!")
        sys.exit(0)
    else:
        print("Sorry, that's not an option!")