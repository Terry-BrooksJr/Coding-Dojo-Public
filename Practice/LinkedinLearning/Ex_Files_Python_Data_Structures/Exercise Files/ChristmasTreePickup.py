"""
This is an exercise I pulled off LinkedIn Learning. The idea is you are running a Christmas tree clean up charity, and are using a Python program to keep track of subdivisions and the number of trees to pick up.

Write a functions that lets the program do the following:
    1. Get the size of the dictionary.
    2. Provide an option to the user to change the number of trees collected from the subdivision. 
    3. Provide an option for the user to add an entry with subdivision ID and number of trees collected. 
    4. print the dictionary using the for and the in  operators in a pretty format
    """

def get_dict_size(dictionary):
    length = len(dictionary)
    return 'There are {length} in this dictionary '


def change_num_trees(dictionary,subdivision_id, num_trees):
    trees_to_be_picked_up = dictionary['subdivision_id'] = num_trees
    return f'(The Number of Trees for subdivision {subdivision_id} has been successfully updated to {trees_to_be_picked_up}.)'


def add_new_customer(dictionary, subdivision_id, num_trees):
#I made this a conditional, becasuse i wanted to account for the use case of its a customer in a subdivision your have and have never collected from 
    if ('subdivision_id' not in dictionary):
        dictionary['subdivision_id'] = num_trees
        return f'added {subdivision_id} to customer list with {num_trees} trees to be picked up'
    elif ('subdivision_id' in dictionary):
        dictionary['subdivision_id'] += num_trees
        return f'Successfully Added a new customer to subdivision {subdivision_id} with {num_trees} trees for pickup. The total for {subdivision_id} is now {dictionary[subdivision_id]}'


def display_all_data(dictionary):
    for subdivision_id in dictionary:
        return('Subdivision ID: {0} - Number of Trees: {1}'.format('Subdivision_id',dictionary['Subdivision_id']))

Print('##############TEST#############')
# print(get_dict_size(mydict))
# print(change_num_trees(mydict,'812',3000))
# print(add_new_customer(mydict,'812',1))
# print(display_all_data(mydict))