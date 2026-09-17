#!/usr/bin/env python3

from cli import collect_user_input ,  display_banner 
from engine import execute_setup
from sys import exit 

def main():
    try : 
        display_banner()
        resultat = collect_user_input()
        if resultat is None :
            exit(0)
        config = resultat[0]
        recipe = resultat[1]
        success = execute_setup(config , recipe)

        if not success :
            print("set up fail. check .newp/setup.log for details.")
            exit(1)
        print("project created successfully!")
        exit(0)
    except KeyboardInterrupt:
        print("\nNEWP cancelled.")
        exit(0)










if __name__ =="__main__":
    main()