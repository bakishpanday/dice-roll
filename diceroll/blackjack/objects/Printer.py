class Printer:
           
    def mainMenu(self):
        print ("The Ultimate Dice Roll Program")
        print()
        print("Be A Responsible Gambler ?")
        print()
        print("Are You Ready To roll....")
        print()
    
    def denyAccess(self):
        print("Access Denied!!! You have to be 19 years or over to play")
    
    def printRollValue(self,value,total):
        print("You rolled A " + str(value) + " Your total rolled number is: " + str(total))
    
    def dieRoll(self,die,ai):
        print("AI's Turn")
        die.roll()
        ai.addToTotal(die.value)
        print("AI Rolled A : " + str(die.value))
        print("Has a total of : " + str(ai.total))

    def playerChoice(self):
        print("would you like to roll another dice or Stand :: If you want to roll select (y) otherwise select (n) ?")  

    def maxTotal(self,main,choice):
        print("Would you like to choose the Maximum Total")
        pick = input("y/n\n")
        if pick =="y":
            int(input("Please Enter your choice:"))
        else: 
            return main()                            