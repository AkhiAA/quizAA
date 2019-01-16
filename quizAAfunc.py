 #quizAAfunc by akhi abdullalh

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
