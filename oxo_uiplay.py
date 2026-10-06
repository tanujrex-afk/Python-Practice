import cmd,oxo_ui,oxo_logic
import argparse as ap
class Oxo_cmd(cmd.Cmd):
    intro="Enter a command: new,resume,quit.type 'help' or'?' for help"
    game=""
    def do_new(self,arg):
        self.game=oxo_logic.newGame()
        oxo_ui.playGame(self.game)
    def do_resume(self,arg):
        self.game=oxo_logic.restoreGame()
        oxo_ui.playGame(self.game)
    def do_quit(self,arg):
        print("Goodbye")
        raise SystemExit
def main():
   game=Oxo_cmd().cmdloop()
   if __name__=="__main__":
        main()
