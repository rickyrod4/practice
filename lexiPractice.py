import random

#"""Make a simple adding challenge for lexi
def calculator():
    for i in range(0,5):
        # declare two random integers
        x = random.randrange(0,10) 
        y = random.randrange(0,10)

        print("what is", x, "*" ,y)
        z = int(input("Your answer is: "))

        if z == x*y:
            print("Yayyyyy you are correct")
        else:
            print("You are a dumbass!")
            print("The correct answer is:", x*y)
        print("-"*50,"\n")

calculator()




    # print those numbers being added
    # get the input from the user
    # check to see if answer is correct
    # print whether user is correct or not"