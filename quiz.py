#creating chatbox todays 
score=0
print(" python quiz")

# Question 1
print("1. Which keyword is used to define a function?")
print("A. function")
print("B. def")
print("C. fun")
print("D. define")
answer = input("Enter your answer: ")
if answer.lower()=="b":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("2. Which data type stores True or False?")
print("A. int")
print("B. str")
print("C. bool")
print("D. float")
answer=input("Enter your answer:")
if answer.lower()=="c":
    print("Correct!")
    score+=1
else:
    print("Wrong!")

# Question 3
print("3. What is the output of 10+20?")
print("A. 20")
print("B. 30")
print("C. 40")
print("D. 10")
answer = input("Enter your answer: ")
if answer.lower()=="b":
    print("Correct!")
    score+=1
else:
    print("Wrong!")
print("quiz finished")
print("Your score:",score,"/3")