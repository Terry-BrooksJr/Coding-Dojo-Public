# Some built-in functions for sequences:
sequence = [15,2,3,5344,3,23,23]
def add_two(sequence):
    for i in sequence:
      return i + 2
enumerate_test = enumerate(sequence) # used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
print(enumerate_test)
map_test = map(add_two, sequence) # applies the function to every item in the sequence you pass in. Returns a list of the results.
print(map_test)
min_test = min(sequence) # returns the lowest value in a sequence.
print(min_test)
sorted(sequence) # returns a sorted sequence
