import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''
# key:value, the comma represents multiple key-value pairs
# the key will always be string (text)
# the value can be anything
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = dict(m=8, n=9)

mydict = {} #how to create an empty dictionary
print(mydictionary)
print(mydict)

print()
print('*****  end section 1 ********')
print()



print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(phonebook[name])

else:
    print(f"{name} is not in the phonebook")

# case sensitive




print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)

# append to the dictionary, if they key does not exist currently, it will be added to the dictionary
# you cannot update the key of a dictionary

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook ['Chris']
print(phonebook)

#del allows us to delete not just the key but they key value pair



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: #phonebook is the name of the dictionary
    print(f" the name is {key} and the phone number is {phonebook[key]}") #to get the value the dictionary needs to have a key
     
for value in phonebook.values():
    print(value) #iterates through phone numbers

    #.values is a method for dictionaries that iterates through the values of the dictionaries
    # this evaluates to a string
for item in phonebook.items():
    print(item) # .items gives us a tuple

for k,v in phonebook.items():
    print(f"the name is {k} and the phone number is {v}")





print()
print('*****  end section 5 ********')
print()


print()
print('*****  start section 6 - using get and clear ********')
print()

#phone = phonebook['chris']
#print(phone)
phone = phonebook.get('chris', '555-0000')
print(phone)

print(phonebook)
phonebook.clear()
print(phonebook)






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

phone = phonebook.pop('Chris', 'not found') #pop method can save but will remove key value from dictionary
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()

print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem() # pulls the last key value pair from the dictionary
print(a)
print(phonebook)




print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

names_list = list(phonebook) #keys are always the default
print(names)
random_key = random.choice(names_list)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))]) #this is a shortcut for random key value




print()
print('*****  end section 9 ********')
print()

