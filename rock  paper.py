import random
print("\t\t\t\tLet's play rock , paper , scissors !!!")
print("\t\t\t\t--------------------------------------",end='\n\n')
print("We'll play it for 3 points")
print("""
press 1: For Rock
press 2: For Paper
press 3: For Scissors
""",end='\n\n')
print("\t\t\t\tLet's get started !!!")
print("\t\t\t\t---------------------",end='\n\n')
count = countn = countm = 0
while count < 3:
    n = random.choice(range(1,4))
    m = int(input("Enter your choice : "))
    if n > 3 or n < 1:
        print("Invalid choice")
    elif m == n:
        print("draw")
        pass
    elif (m == 1 and n == 2) or (m == 2 and n == 3) or (m == 3 and n == 1):
        print("user + 1")
        countn += 1
        count += 1
    elif (m == 1 and n == 3) or (m == 2 and n == 1) or (m == 3 and n == 2):
        print("computer + 1")
        countm += 1
        count += 1
print("user score = {}".format(countn))
print("computer score = {}".format(countm))
if countm > countn:
    print("computer wins")
else:
    print("user wins")
