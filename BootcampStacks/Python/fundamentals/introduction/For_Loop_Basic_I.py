print('###################Basic#####################################')
#Basic - Print all integers from 0 to 150.
for x in range(151):
    print(x)
print('###################Multiples of Five clear#####################################')
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(0,1001,5):
    print(x)
print('###################Counting, the Dojo Way#####################################')
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(101):
    if x % 10 == 0:
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)
print('###################Whoa. That Sucker is Huge#####################################')
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for x in range(500000):
    acc = 0
    if x % 2 != 0:
        acc = acc + x
        print(acc)
        
print('###################Countdown By Fours#####################################')

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    print(x)
print('###################Flexible Counter#####################################')
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
low_num = 0
high_num = 201
mult = 5

for x in range(low_num,high_num+1):
    if x % mult == 0:
        print(x)