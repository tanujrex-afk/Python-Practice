import cmd
class Oxo_cmd(cmd.Cmd):
    intro="enter a command:new,resume,quit. Type 'help' or '?' for help"
    prompt="(oxo)"
def do_new(self,arg):
    print("starting new game")
def do_restore(self,arg):
    print("Restoring prevous game")
def do_quit(self,arg):
    print("Goodbye....")
    raise SystemExit
def main():
    game=Oxo_cmd().cmdloop()
if __name__=="__main__":
    main()
