string = "This is a Test, Only a Test!";
substring = string.split();
list = [12,4,4,23,54]

upper_test = string.upper()# returns a copy of the string with all the characters in uppercase.
print(upper_test)
lower_test = string.lower()# returns a copy of the string with all the characters in lowercase.
print(lower_test)
count_test = string.count(substring)# returns number of occurrences of substring in string.
print(count_test)
string.split(char)# returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
print(substring)
find_test = string.find(substring)# returns the index of the start of the first occurrence of substring within string.
print(find_test)
string.isalnum()# returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
join_test = string.join(list)# returns a string that is all strings within our set (in this case a list) concatenated.
print(join_test)
string.endswith(substring)# returns a boolean based upon whether the last characters of string match substring.