#coding:utf-8

total = 0
for i in xrange(100):
    if i % 2 == 0:
        total = total + i
print total

def sumOfEven(num):
    total = 0
    for i in xrange(num):
        if i % 2 == 0:
            total = total + i
    return total

print sumOfEven(100)

def sumOfAll(num):
    total = 0
    for i in xrange(num):
        total += i
    return total

print sumOfAll(100)
