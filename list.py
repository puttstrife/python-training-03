users = ['Aave', 'John', 'Sara', 'Robert']  # list of users

data = ['Aave', 42, True]  # this is also a valid list


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

# users.extend(data)
# print(users)


# users.insert(0, 'Bob')
# print(users)

# users[2:2] = ['Eddie', 'Alex']
# print(users)


# users[1:3] = ['Robert', 'JPJ']
# print(users)


# users.remove('Bob')  # remove data
# print(users)

# print(users.pop(2))

# del users[0]  # delete data
# print(users)


# del data  # this can't delete the list
# print(data)


# data.clear()
# print(data)  # this will clear the list but not deleting it


users[1:2] = ['dave']
users.sort()
print(users)


users.sort(key=str.lower)  # incluse lowercase in alphabetical order
print(users)


nums = [4, 42, 78, 1, 5]
# nums.sort()
# print(nums)


# nums.sort(reverse=True)  # it will sort it descending instead of ascending
# print(nums)

# global sorted function # ' nums, ' call that on the nums list and pass the options ' reverse=True '
# print(sorted(nums, reverse=True))
# print(nums)


# list is just like the array in Javascript


numscopy = nums.copy()
mynums = list(nums)  # ' list ' the constructor
# specify the index range do not specify the beginning and the end
mycopy = nums[:]

print(numscopy)
print(mynums)

mycopy.sort()
print(mycopy)
print(nums)


mylist = list([1, 'Neil', True])
print(mylist)

# Tuples are like list except the data in tuples will not change and also the order will not change

mytuple = tuple(['Dave', 42, True])
# if you use parenthesis not brackets it is a tuple list
anotherTuple = (1, 2, 4, 8, 2, 2, 8, 88)
notATuple = [1, 2, 3, 4]  # now this one is just a list
print(mytuple)
print(type(mytuple))
print(type(anotherTuple))
print(type(notATuple))

newList = list(mytuple)  # this will create a new list out of the tuple

newList.append('Neil')  # you can unpacked a tuple

newTuple = tuple(newList)
print(newTuple)
print(type(newTuple))

# unpacking tuples

(one, two, *hey) = anotherTuple
print(one)
print(two)
print(hey)
# the 'count' counting the occurances of the number 8
print(anotherTuple.count(8))  # tuple only have 2 methods
