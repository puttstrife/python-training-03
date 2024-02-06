users = ['Dave', 'John', 'Sara', 'Robert']  # list of users

data = ['Dave', 42, True]  # this is also a valid list


emptyList = []  # An empty list is also a valid list

print(users[0])

print(users.index('Sara'))  # use method to know the specific value

print(users[0:2])
# living the end range blank means it will show all string to the right until the last string
print(users[1:])
print(users[-3:-1])  # we can use negative

print(len(users))  # Len is length function

# adding list

users.append('Elsa')  # apppend is a method to add a string / data
print(users)

users += ['Jason']

print(users)

users.extend(['Jimmy', 'Alan'])  # like append extend can add data/string
print(users)

# you can pass in a existing list

users.extend(data)
print(users)
