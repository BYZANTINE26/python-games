import random
import numpy
import string
l = int(input("Desired length of your password (min 6) : "))
if l < 6:
    print("Invalid choice !!")
else:
    n = int(input("How many numbers do you want in your password : "))
    z = (l - n) - 2
    t = ['!','@','#','$','%','^','&','*']
    r = list(string.ascii_lowercase)
    s = list(string.ascii_uppercase)
    li = r + s
    #li.append(r)
    #li.append(s)
    x = []
    for w in range(z):
        b = random.choice(li)
        x.append(b)
    for f in range(2):
        h = random.choice(t)
        x.append(h)
    for i in range(n):
        d = random.choice(range(10))
        x.append(d)
    random.shuffle(x)
    for j in range(len(x)):
        print(x[j],end='')
