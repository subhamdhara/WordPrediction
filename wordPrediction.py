import random
import time

words = list({'rainbow', 'computer', 'science', 'programming',
              'python', 'mathematics', 'player', 'condition',
              'reverse', 'water', 'board', 'food', "bench", "chair", "table",
              "spell", "java", "ruby", "rugby", "football", "oak",
              "rain", "pain"})

r = random.choice(words)

print("Guess the characters")
for _ in range(len(r)):
    print("-")
    time.sleep(0.30)
userW = []

for i in range(len(r)):
    user = input("Enter the character: ")
    while user != r[i]:
        if user == "hint":
            print("starts with", r[0])
        else:
            print("try again")
        user = input("Enter the character: ")

    userW.append(user)

    for i in range(len(r)):
        try:
            print(userW[i])
        except IndexError:
            print("-")
else:
    print("You got it correct, it's", r)