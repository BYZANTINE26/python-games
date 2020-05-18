#import numpy
#import random
# x = [['pass','countn+=1','countm+=1'],['countm+=1','pass','countn+=1'],['countn+=1','countm+=1','pass']]
# a = numpy.array(x)
#count = countn = countm = 0
#while count < 3:
#    m = random.choice(range(3))
#    n = int(input("Enter your choice : "))
#    eval(a[m][n])
#    if a[m][n]=='countm+=1' or a[m][n]=='countn+=1':
#        count+=1
#print("m = {}".format(countm))
#print("n = {}".format(countn))
# y=eval(a[0:3 , 0:3])
# print(y)
import string
import random
l = list(string.ascii_lowercase)
m = list(string.ascii_uppercase)
ab = l + m
#ab.append(l)
#ab.append(m)
b = random.choice(ab)
print(ab)
