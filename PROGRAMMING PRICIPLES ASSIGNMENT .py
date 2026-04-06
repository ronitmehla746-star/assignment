import random
import math
print("WELCOME TO THE MATHEMATICS TEST")
NAME = input("Enter your name: ")
STUDENT_ID = int(input("Enter your student id: "))
UNIT = input("Enter your unit name: ")
SUBMITTED_TO = input("Enter your tutor name: ")

def make_list(n, low, high):
    l = []
    for i in range(n):
        l.append(random.randint(low, high))
    return l

while True:
    d = input("Enter difficulty (easy/medium/hard): ").lower()
    if d == "easy" or d == "medium" or d == "hard":
        break
    else:
        print("Wrong input, try again")

if d == "easy":
    q = 3
    size = 3
    low = 1
    high = 10
elif d == "medium":
    q = 5
    size = 4
    low = 5
    high = 15
else:
    q = 7
    size = 5
    low = 10
    high = 20

print("\nTest info:")
print("Questions:", q)
print("List size:", size)
print("Range:", low, "-", high)

input("Press Enter to start...")

score = 0
used_lst = []

for i in range(q):
    print("\nQ", i+1)
    
    lst = make_list(size, low, high)
    print(lst)
   
    t = random.choice(["max", "min", "sum","product"])

    if t == "max":
        ans = int(input("Find max: "))
        correct = max(lst)
    elif t == "min":
        ans = int(input("Find min: "))
        correct = min(lst)
    elif t == "sum":
        ans = int(input("Find sum: "))
        correct = sum(lst)
    else:
        t == "product"
        ans = int(input("Find product: "))
        correct = math.prod(lst)
    if ans == correct:
        print("Right")
        score += 1
    else:
        print("Wrong, answer =", correct)

print("\nScore:", score, "/", q)
