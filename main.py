print("Welcome to LnT Mini Quiz!")

play = int(input("1. Start Game \n2. Exit \n"))
if play != 1: 
    quit()

print("There are a total of 5 questions. Each correct answer will gives you one point. Good luck!")
score = 0

answer = input("1. What does LnT stands for? \na. Learning and Training \nb. Learn and Try \n>> ")
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("2. How many members are in the LnT subdivision? \na. Four \nb. Five \n>> ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("3. Who is the PIC for regeneration in LnT subdivision? \na. Indra \nb. Jansen \n>> ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("4. In internal BNCC, who is a praetorian that teaches UI/UX? \na. Bertrand \nb. Michael Dinata \n>> ")
if answer.lower() == "a":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("5. Which of these are not the LnT's module development steps? \na. Weekly Standup \nb. Quality Control \n>> ")
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You answered " + str(score) + " question(s) correctly!")
print("Your score is " + str(score * 20) + "!")