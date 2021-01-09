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
