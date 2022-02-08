#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
from re import X
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #creating a dictionary - walk through code.
   # And introduce the idea of a Case Study
    mydict ={}
    

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
        2
   
    
    infile.close()

def get_dict_size(dictionary):
    return len(dictionary)


def change_num_trees(dictionary,subdivision_id, num_trees):
    trees_to_be_picked_up = dictionary['subdivision_id'] = num_trees
    return f'(The Number of Trees for subdivision {subdivision_id} has been successfully updated to {trees_to_be_picked_up}.)'


def add_new_customer(dictionary, subdivision_id, num_trees):
    if (subdivision_id in dictionary):
        dictionary['subdivision_id']  += num_trees
        new_total = dictionary['subdivision_id'][subdivision_id]
        return f'Successfully Added a new customer to subdivision {subdivision_id} with {num_trees} trees for pickup. The total for {subdivision_id} is now {new_total}'
    else:
        return f'{subdivision_id} Not Found'

def display_all_data