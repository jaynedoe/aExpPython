#control flow in python - if statements

number = 88

if number > 10:
    print("Number is greater than 10")
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is less than 10.")

#iterators in python - for-in loops

listicle = ["jae", "karina", "michael"]

print("\nPrints from a for-in loop:")

for name in listicle:
    print("Hi %s" % name)

#ranges in python

print("\nPrints a range:")

for x in range(5):
    print("The count is %d" % x)

print(range(5))

#iterators in python - while loop

i = 0

print("\nPrints using a while loop")

while(i < 10):
    print(i)
    i = i+1

# ---------------LISTS----------------------
 
# lists - mutable, any data type, created with square brackets, in order

jaeInterests = ['philosophy', 'german', 'data science', 'web development', 'sustainability', 'fitness', 'nature']

#traversing a list using a for loop:

for interest in jaeInterests:
    print(interest + " is an interest of Jae.")

#length of a list:

print(len(jaeInterests))

#accessing the value at a particular index position: 

print(jaeInterests[2] + ": this should have printed data science.")

#slicing a list:

newList = jaeInterests[1::2]
print(newList)

#searching for a particular value within the items of a list - returning true or false:

print("german" in jaeInterests)  #returns true

#list methods - appending

jaeInterests.append("lego")

#print the last item in the list to check it has been appended:

print(jaeInterests[-1])

#sort the list alphabetically - CHANGES ORIGINAL LIST!:

jaeInterests.sort()
print(jaeInterests)

#sort the list alphabetically - CREATES NEW LIST AND LEAVES ORIGINAL IN TACT:

newList = sorted(jaeInterests)
print(newList)
    
#take a string, split it according to a delimiter and store individuals in a list:

stringy = "I am a stringy string string."
s = stringy.split(" ")
print(s) # prints ["I", "am", "a", "stringy", "string", "string."]

#rejoin the list items together in one string using the join method on the delimiter:

a = " ".join(s)
print(a) # prints "I am a stringy string string"

#-------------------TUPLES----------------------------------------------------------

#Tuples are similar to lists except they are not mutable - cannot be changed once created.
#Are created using curved braces.  They are a data sequence IN ORDER, like lists.

riley = ("Riley", "Icecream", 4, "AT-AT")
link = ("Lincoln", "Pasta", 2, "Whale")
harry = ("Harry", "Pink Milk", 5, "Push Bike")

(name, favouriteFood, age, favouriteToy) = riley
(name, favouriteFood, age, favouriteToy) = link

print(riley) #prints ("Riley", "Icecream", 4, "AT-AT")
print(name) #prints "Lincoln", since the variable 'name' is overwritten

print(riley[3]) #prints "AT-AT"

nephews = [riley, link, harry] # a list of tuples
print(nephews[1][3]) #prints "whale"

for nephew in nephews:
    print("The name of my nephew is: " + nephew[0])
    #prints  "The name of my nephew is: Riley
            #"The name of my nephew is Lincoln
            #"The name of my nephew is Harry


#-------------------DICTIONARIES----------------

#Are mutable but not ordered - consist instead of key value pairs where the keys are unique and used to identify values
#Keys must be immutable types - strings or tuples
#Values can be mutable or immutable
#Dictionaries are created using curly braces.

nephewDictionary = {riley: "is my favourite.", link:"is also my favourite.", harry: "is a good boy, I just don't see him much."}

print(nephewDictionary[riley]) #prints "is my favourite"
print(nephewDictionary[harry]) #prints "is a good boy"

#traverse a dictionary using for in loops:

for key in nephewDictionary:
    print(key[0], nephewDictionary[key])
    #prints "Riley is my favourite."
    #       "Lincoln is also my favourite."
    #       "Harry is a good boy, I just don't see him much."