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

#question5
q5= """QA:Whats Akhis Favorite Color?
1)Pink
2)Navy Blue
3)Turquoise
4)Lavender
"""
a5 = int(0)
check5 = bool(False)
q5Ans = 2

#question6
q6=""" QA:What Zodiac Sign Is Akhi? 
1)Capricorn
2)Saggitarius
3)Leo
4)Cancer
"""
a6 = int(0)
check6 = bool(False)
q6Ans = 4

#question7
q7="""QA:Whats Akhis Eye Color
1)black
2)dark brown
3)brown 
4)light brown 
"""
a7 = int(0)
check7 = bool(False)
q7Ans = 3

#question8
q8=""" QA:What Type Of Consol Does Akhi Play?
1)Xbox
2)Pc
3)Wii
4)Playstation 
"""
a8 = int(0)
check8 = bool(False)
q8Ans = 4

#question9
q9="""QA:What College Does Akhi Want To Go To?
1)Marist
2)Colombia
3)NYU
4)MIT
"""
a9 = int(0)
check9 = bool(False)
q9Ans = 2

#question10
q10="""QA:What is Akhis Favorite Type Of Food?
1)Halal Cart food 
2)Indial Food
3)Turkish Food
4)Chicken 
"""
a10 = int(0)
check10 = bool(False)
q10Ans = 3

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
    print ("wow you almost got a perfect score")
elif grade == 8: #80%
    print("Not bad .. Not bad")
elif grade == 7: #70%
    print("you onlly got 3 questions wrong.. thats fine")
elif grade == 6: #60%
    print("try harder next time")
elif grade == 5: #50%
    print("wow you only got half the questions wrong")
elif grade == 4: #40%
    print("I think you should try to get to know me better")
elif grade == 3: #30%
    print("I dont think we've meet")
elif grade == 2: #20%
    print(" You shold try to get to know me better")
elif grade == 1: #10%
    print("Hi my name is akhi, i dont think we've meet")
elif grade == 0: #0%
    print("who are you")
else:
    print ( "try agin using a positive integer!")  # If the user does not input an integer

