num1 = 42  # variable declaration, interger, initialize
num2 = 2.3  # variable declaration, float, initialize
boolean = True  # variable declaration, boolean, initialize
string = 'Hello World'  # variable declaration, initialize, str
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives']  # variable declaration, initialize, list
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}  # variable declaration, initialize,  dict
fruit = ('blueberry', 'strawberry', 'banana')  # variable declaration, tuple
print(type(fruit))  # Tuples, access value
print(pizza_toppings[1]) # Accessing series 
pizza_toppings.append('Mushrooms')  # change value
print(person['name'])  # List˜, access value
person['name'] = 'George' #List, change value
person['eye_color'] = 'blue'  # List, change value
print(fruit[2])  # List, Access Value

if num1 > 45:  #conditional, if/else
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #conditional, else if 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop, start
    print(x)
for x in range(2,5): #for loop  start  Range 
    print(x)
for x in range(2,10,3): #for loop, start Range 
    print(x)
x = 0
while(x < 5): #While loop, start
    print(x)
    x += 1

pizza_toppings.pop() #List, Value Change last Item 
pizza_toppings.pop(1) #List, Value Change, 2nd Item

print(person)  #Funtion, Value Access
person.pop('eye_color') #List Value Change
print(person)  # Funtion, Value Access

for topping in pizza_toppings: #For Loop Start
    if topping == 'Pepperoni': # Expression, Conditional Accessing Equality
        continue #Continue Keyword 
    print('After 1st if statement') 
    if topping == 'Olives':  # Expression, Conditional Accessing Equality
        break #ke ywored
def print_hello_ten_times():  #function definition 
    for num in range(10):
        print('Hello')
2
print_hello_ten_times() #Un-argmented function call 


def print_hello_x_times(x):  # function definition
    for num in range(x):
        print('Hello')


print_hello_x_times(4)  # -argmented function call


def print_hello_x_or_ten_times(x=10):  # function definition
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()  # Un-argmented function call


print_hello_x_or_ten_times(4)  # argmented function call




"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)