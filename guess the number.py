import random as rn
print("\t\t\t\t\tHey let's play a game !")
print("\t\t\t\t\t-----------------------",end='\n\n')
print(""""How does  it sounds !!
I'll pick a number randomly between 1 to 10 and you have to guess it !!!""")
ap = 0
while True:
    n = rn.choice(range(1,11))
    print("Enter the number you guessed :",end=' ')
    m = int(input())
    if m == n:
        print("Yes , it's correct !")
    elif m > n:
        print("Subtract {} from {}".format(m-n,m))
        ap = round(((m-n)/n)*100,2)
    elif m < n:
        print("Add {} to {}".format(n-m,m))
        ap = round((((-1)*(n-m))/n)*100,2)
    print("you were {}% wrong".format(ap))
    print("Press 1: To play again")
    print("Press 2: To Quit")
    ch = int(input())
    if  ch == 2:
        break
