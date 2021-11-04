# task 6.1
# print([i for i in range(3,-1,-1)])

# task 6.2
"""
guess_me = 7
number = 1
while True:
    if guess_me > number:
        print("too low")
    elif guess_me == number:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1
"""

print("# task 6.3")
guess_me = 5
for number in range(10):
    if guess_me > number:
        print("too low")
    elif guess_me == number:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1
