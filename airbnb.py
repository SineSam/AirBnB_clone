#!/usr/bin/python3
import cmd

class Console(cmd.Cmd):
        intro = "Welcome to AirBnB"
        prompt = "Console"

        def do_command(self, args):
            pass
if __name__ == "__main__":
    Console().cmdloop()
