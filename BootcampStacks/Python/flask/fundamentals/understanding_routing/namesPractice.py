from names import names
from random import randrange

for name in names:
    random_name = names[randrange(51)]
    print(f'Welcome to the World Wide Web, I am your Web Server, {random_name}')
    user_name = input('What is your Name?')
    print(f'Great to meet you {user_name}, What am I serving up')
