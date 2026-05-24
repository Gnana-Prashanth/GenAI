import os
import random

#print("Welcome to AI Quiz Generator 😎")
name = input("Enter your name:")

file = open("questions.txt", "r")

questions = file.readlines()

file.close()

random.shuffle(questions)

score = 0

print("=" * 40)
print("🤖 Welcome to AI Quiz Generator 🤖")
print("=" * 40)

for line in questions:
    parts = line.strip().split("|")
    if len(parts) == 2:

        question, answer = parts
        user_answer = input(question + " : ")

        if user_answer.lower() == answer.lower():
            print("Correct✅\n")
            score += 1

        else:
            print("Wrong❌")
            print("Correct Answer:", answer, "\n")

print("🚧📍 Your Final Score is:",score,"/10  ✨✨")

score_file = open("scores.txt", "a")

score_file.write(name + " : " + str(score) + "\n")

score_file.close()