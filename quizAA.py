#quizAA by akhi abdullalh
#global grade 
global grade
grade = 0

#Imported files 
from quizAAdata import *

#quizAAfunc
# Define question/answer function.
def run_qa_loop(qStr, qCheck, ansU, ansCor):
    print(qStr)

    while qCheck == False:
        try:
            ansU = int(input("Choose 1, 2, 3, or 4 Based on your thoughts.  ")) 
            if ansU == ansCor:
                print("Thanks")  #acceptable answer
                global grade
                grade += 1
                qCheck = True
            elif 0 < ansU < 5:  #acceptable answer 
                print ("Thanks")
                qCheck = True
            else:
                print (" Please enter an integer from 1-4 ")  #non-acceptable answer
        except ValueError:
            print (" Come on now, Just try ")

#intro
print("Welcome to my quiz where you will be asked 10 questions")
print("Each question will have 4 multiple choces")
print ("All of these questions will be based on how well you know Akhi")
print("Good Luck")
print()

#Question1-4
run_qa_loop(q1, a1, check1, q1Ans)
run_qa_loop(q2, a2, check2, q2Ans)
run_qa_loop(q3, a3, check3, q3Ans)
run_qa_loop(q4, a4, check4, q4Ans)
#Question5-8
run_qa_loop(q5, a5, check5, q5Ans)
run_qa_loop(q6, a6, check6, q6Ans)
run_qa_loop(q7, a7, check7, q7Ans)
run_qa_loop(q8, a8, check8, q8Ans)
#Question9-10
run_qa_loop(q9, a9, check9, q9Ans)
run_qa_loop(q10, a10, check10, q10Ans)


#score
print( "you got", grade *10, "%")

if grade == 10: #100%
    print("Great job, you really know me")
elif grade == 9: #90%
    print ("Wow you almost got a perfect score")
elif grade == 8: #80%
    print("Not bad .. Not bad")
elif grade == 7: #70%
    print("You onlly got 3 questions wrong.. thats fine")
elif grade == 6: #60%
    print("Try harder next time")
elif grade == 5: #50%
    print("Wow you only got half the questions wrong")
elif grade == 4: #40%
    print("I think you should try to get to know me better")
elif grade == 3: #30%
    print("I dont think we've meet")
elif grade == 2: #20%
    print(" You shold try to get to know me better..")
elif grade == 1: #10%
    print("Hi my name is Akhi,i dont think we've meet")
elif grade == 0: #0%
    print("Who are you?")
else:
    print ( "try agin using a positive integer!")  # If the user does not input an integer

