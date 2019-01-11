 #quizAA by akhi abdullalh

global grade
grade = 0

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
            
# initialize variables
score = int(0)

#First Question 
q1 = """QA: Where is Akhi from?
1) Dominican republic 
2) Arabic 
3) India
4) Bangladesh
"""
a1 = int(0)
check1 = bool(False)
q1Ans = 4

#question2
q2 = """QA: Whens Akhis Birthday?
1) July 11th 
2) January 4th
3) April 30th
4) June 16th 
"""
a2 = int(0)
check2 = bool(False)
q2Ans = 1

#question3
q3 = """QA:How Tall is Akhi? 
1) 5'3
2) 5'4
3) 5'5
4) 5'3.5
"""
a3 = int(0)
check3 = bool(False)
q3Ans = 3

#Question4
q4 = """ QA: What Is Akhi's Favorite Subject? 
1)Math
2)Science
3)English
4)History 
"""
a4 = int(0)
check4 = bool(False)
q4Ans = 1
#intro
print("Welcome to my quiz where you will be asked 10 questions")
print("Each question will have 4 multiple choces")
print ("All of these questions will be based on how well you know Akhi")
print("Good Luck")
print()

#Question1
run_qa_loop(q1, a1, check1, q1Ans)

#Question2
run_qa_loop(q2, a2, check2, q2Ans)

#Question3
run_qa_loop(q3, a3, check3, q3Ans)

#Question4
run_qa_loop(q4, a4, check4, q4Ans)

#score
print( "you got", grade *25, "%")



