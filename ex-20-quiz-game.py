# Quiz game Program

questions = ("1. How many elements are in the periodic table?: ", 
             "2. Which animal lays the largest eggs?: ", 
             "3. What is the most abundant gas in Earth's atmosphere?: ", 
             "4. How many bones are there in the human body?: ", 
             "5. Which planet in the solar system is the hottest?: ")     # 1D array tupple

options = (("A. 116", "B. 117", "C. 118", "D. 119"),                    
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 210", "C. 211", "D. 212"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))             # 2D array tupple

answers = ("C", "D", "A", "A", "B")

guesses = []                                                              # 1D array list

score = 0

question_num = 0

for question in questions:
    print("--------------------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1

    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")        


    question_num += 1  

print("------------------------------")
print("          Result              ")
print("------------------------------")

print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()

score = int(score/len(questions) * 100)
print(f"Your total score is {score}%")