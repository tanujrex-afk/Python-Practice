import tkinter
import tkinter.messagebox as mb
import oxo_logic
menu=["Start new gamee",
      "Resume saved game",
      "Display help",
      "Quit"]
def getMenuChoice(aMenu):
    if not aMenu:raise ValueError('No menu content')
    while True:
        print("\n\n")
        for index, item in enumerate(aMenu,start=1):
            print(index,"\t",item)
        try:
            choice=int(input("\n Choose a menu Option:"))
            if 1<=choice<=len(aMenu):
                return choice
            else:print("choose a number between 1 and ",len(aMenu))
        except ValueError:
            print("choose the number of menu option")
def main():
    top=tkinter.Tk()
    top.withdraw()
    while True:
        choice=getMenuChoice(menu)
        executeChoice(choice)
  

def startGame():
    return oxo_logic.newGame()
def resumeGame():
    return oxo_logic.restoreGame()
def displayHelp():
    print('''start new game: starts a new game of tic-tac-toe
             Resume saved game: restores the last saved game and comences play
             Display help: shows this page
             Quit: quits the application''')
def quit():
    print("GoodBye")
    raise SystemExit
def executeChoice(choice):
    dispatch=[startGame,resumeGame,displayHelp,quit]
    game=dispatch[choice-1]()
    if game:
        pass
def printGame(game):
    display='''
            1|2|3   {}|{}|{}
            -----   --------
            4|5"6   {}|{}|{}
            -----   --------
            7|8|9   {}|{}|{}'''
    print(display.format(*game))
def playGame(game):
    result=""
    while not result:
        printGame(game)
        choice=input("Cell[1-9 or q to quit]:")
        if choice.lower()[0]=='q':
            save=mb.askyesno("Save game","save game before quitting?")
            if save:
                oxo_logic.saveGame(game)
                quit()
            
        else:
            try:
                cell=int(choice)-1
                if not(0<=cell<=8):
                    raise ValueError
            except ValueError:
                print("choode a number between 1 and 9 or q to quit")
                continue
            try:
                result=oxo_logic.userMove(game,cell)
            except ValueError:
                mb.showerror("Invalid cell","choose an empty cell")
                continue
            if not result:
                result=oxo_logic.computerMove(game)
            if not result:
                continue
            elif result=='D':
                printGame(game)
                mb.showinfo("Result","Its a Draw")
            else:
                printGame(game)
                mb.showinfo("Result","Winner is{}".format(result))

