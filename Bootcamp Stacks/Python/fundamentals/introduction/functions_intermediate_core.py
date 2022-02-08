print('######################Update Values in Dictionaries and Lists###############################')
x = [ [5,2,3], [10,8,9] ]  
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
z[0]['x'] = 15
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres' Change the value 20 in z to 30
sports_directory['soccer'][0] = 'Messi'
sports_directory['basketball'][0] = 'Jordan'
print(x)
print(students)
print(sports_directory)
print(z)
print('########################### Iterate Through a List of Dictionaries #######################')
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(list_of_dictionaries):
    for x in list_of_dictionaries:
        for value,key in 
    # keys = dictionary[0].keys()
    # values = dictionary[0].values()
    # for values[x] in values:
    #     print(f'{keys[0]} - {values[x]}, {keys[1]} - value[x]')


print(iterateDictionary(students))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
