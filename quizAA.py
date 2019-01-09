#quizAA by akhi abdullalh 
#quizAA by akhi abdullalh
#First Question 
# initialize variables
q1 = """QA: Where is Akhi from 
1) Dominican republic 
2) Arabic 
3) India
4) Bangladesh
"""

a1 = int(0)
check1 = bool(False)
score = int(0)

#question2
q2 = """QA: Whens Akhis Birthday
1) July 11th 
2) January 4th
3) April 30th
4) June 16th 
"""
a2 = int(0)
check2 = bool(False)

#question3
q3 = """QA:How Tall is Akhi 
1) 5'3
2) 5'4
3) 5'5
4) 5'3.5
"""
a3 = int(0)
check3 = bool(False)

#intro
print("Welcome to my quiz where you will et asked 10 questions")
print("Each question will have 4 multiple choces")
print ("All of these questions will be bsed on how wel you know Akhi")
print("Good Luck")
print()

# question1
print(q1)

while check1 == False:
    try:
        a1 = int(input("Choose 1, 2, 3, or 4 Based on your thoughts.  ")) 
        if a1 == 4:
            print("Thanks")  #acceptable answer
            score=int(score+1)
            check1 = True
        elif 0 < a1 < 5:  #acceptable answer 
            print ("Thanks")
            check1 = True
        else:
            print (" Please enter an integer from 1-4 ")#non-acceptable answer
    except ValueError:
        print (" Come on now, Just try ")
        
#Question2
print(q2)
while check2 == False:
    try:
        a2 = int(input("Choose 1, 2, 3, or 4 Based on your thoughts.  ")) 
        if a2 == 1:
            print("Good") #acceptable answer
            score=int(score+1)
            check2 = True
        elif 0 < a2 < 5:  #acceptable answer 
            print ("Good")
            check2 = True
        else:
            print (" Please enter an integer from 1-4 ")  #non-acceptable answer
    except ValueError:
        print (" Come on now, Just try ")

#Question3
print(q3)
while check3 == False:
    try:
        a3 = int(input("Choose 1, 2, 3, or 4 Based on your thoughts.  ")) 
        if a2 == 2:
            print("Good") #acceptable answer
            score=int(score+1)
            check3 = True
        elif 0 < a3 < 5:  #acceptable answer 
            print ("Good")
            check3 = True
        else:
            print (" Please enter an integer from 1-4 ")  #non-acceptable answer
    except ValueError:
        print (" Come on now, Just try ")        
        
#score
print("quiz score: ",score * 33, "%")



