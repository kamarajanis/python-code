import random
x=int(input("Guess and Enter that Number\n"))
y=random.randint(0,3)
if x==y:
    print("Correct")
else:
    print("Wrong")
    print("The Answer is");print(y)    
    

