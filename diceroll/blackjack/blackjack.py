
from objects import Player, Die, Printer
def main():
     
    printer = Printer.Printer()
    printer.mainMenu()
    choice = 0
    choice = int(input("Please Enter Your Age:"))
    if choice < 19:
        printer.denyAccess()
        return
    
    else: 
        print("Access Granted")  
        turn = "player"
        player = Player.Player()
        ai = Player.Player()
        die = Die.Die()
        maxTotal = (choice)

    
    while True:
            if turn == "player":
                print("die rolling \../")
                if player.total == 0:
                    for i in range(2):
                        die.roll()
                        player.addToTotal(die.value)
                    print(player.total)
                else:
                    printer.playerChoice() #adding class to die roll
                    pick = input("y/n\n")
                    print("AI is rolling the dice")
                    if pick == "y":
                        die.roll()
                        player.addToTotal(die.value)
                        printer.printRollValue(die.value,player.total)
                        if player.total > maxTotal:
                            print("Player has busted and lost, so sad ( >_< -_- >_< -_-)")
                            break
                    else:
                        print("Your Total is : " + str(player.total))
                        turn = "AI"
            else: # AI turn logic
                
                printer.dieRoll(die,ai)
                if ai.total >= player.total and ai.total <= maxTotal:
                    print("AI Wins  >_< -_- >_< -_-")
                    break
                elif ai.total > maxTotal:
                    print("AI busted @-@ you got lucky =^_^= ")
                    break
                else:
                    pass
    print("Thanks for playing! Would You Like To Play Again")
    pick = input("y/n\n")
    if pick == "y":
        return main()
    else:
        return print("Have A Great Day !! See You Soon")  
    





if __name__ == "__main__":
    main()


