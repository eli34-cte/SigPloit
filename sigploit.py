#!/usr/bin/env python
'''
SigPloit Main

Created on 1 Feb 2018

@author: loay

@license:    MIT license
'''

import sys
import os
import time
import sys
import signal

def banner(word):
    letterforms = r'''\
       |       |       |       |       |       |       | |
  XXX  |  XXX  |  XXX  |   X   |       |  XXX  |  XXX  |!|
  X  X |  X  X |  X  X |       |       |       |       |"|
  X X  |  X X  |XXXXXXX|  X X  |XXXXXXX|  X X  |  X X  |#|
 XXXXX |X  X  X|X  X   | XXXXX |   X  X|X  X  X| XXXXX |$|
XXX   X|X X  X |XXX X  |   X   |  X XXX| X  X X|X   XXX|%|
  XX   | X  X  |  XX   | XXX   |X   X X|X    X | XXX  X|&|
  XXX  |  XXX  |   X   |  X    |       |       |       |'|
   XX  |  X    | X     | X     | X     |  X    |   XX  |(|
  XX   |    X  |     X |     X |     X |    X  |  XX   |)|
       | X   X |  X X  |XXXXXXX|  X X  | X   X |       |*|
       |   X   |   X   | XXXXX |   X   |   X   |       |+|
       |       |       |  XXX  |  XXX  |   X   |  X    |,|
       |       |       | XXXXX |       |       |       |-|
       |       |       |       |  XXX  |  XXX  |  XXX  |.|
      X|     X |    X  |   X   |  X    | X     |X      |/|
  XXX  | X   X |X     X|X     X|X     X| X   X |  XXX  |0|
   X   |  XX   | X X   |   X   |   X   |   X   | XXXXX |1|
 XXXXX |X     X|      X| XXXXX |X      |X      |XXXXXXX|2|
 XXXXX |X     X|      X| XXXXX |      X|X     X| XXXXX |3|
X      |X    X |X    X |X    X |XXXXXXX|     X |     X |4|
XXXXXXX|X      |X      |XXXXXX |      X|X     X| XXXXX |5|
 XXXXX |X     X|X      |XXXXXX |X     X|X     X| XXXXX |6|
XXXXXX |X    X |    X  |   X   |  X    |  X    |  X    |7|
 XXXXX |X     X|X     X| XXXXX |X     X|X     X| XXXXX |8|
 XXXXX |X     X|X     X| XXXXXX|      X|X     X| XXXXX |9|
   X   |  XXX  |   X   |       |   X   |  XXX  |   X   |:|
       |       |       |       |       |       |       |^|
'''.splitlines
        table = {}
    for form in letterforms.splitlines():
        if '|' in form:
            table[form[-2]] = form[:-3].split('|')

    ROWS = len(list(table.values())[0])

    for row in range(ROWS):
        for c in word:
            print(table[c][row], end=' ')
        print()

def mainMenu():
    os.system('clear')

    banner('SigPloit')
    print("\033[33m[-][-]\033[0m\t\tSignaling Exploitation Framework\t\033[33m [-][-]\033[0m")
    print("\033[33m[-][-]\033[0m\t\t\tVersion:\033[31mBETA 1.1\033[0m\t\t\033[33m [-][-]\033[0m")
    print("\033[33m[-][-]\033[0m\t\tAuthor:\033[32mLoay AbdelRazek(@sigploit)\033[0m\t\033[33m [-][-]\033[0m\n")
    print("Contributors:")
    print("\t\033[31mRosalia D'Alessandro\033[0m")
    print("\t\033[31mIlario Dal Grande\033[0m")
    print("\n")

    print("   Module".rjust(10) + "\t\t\tDescription")
    print("   --------                --------------------")
    print("0) SS7".rjust(8) + "\t\t2G/3G Voice and SMS attacks")
    print("1) GTP".rjust(8) + "\t\t3G/4G Data attacks")
    print("2) Diameter".rjust(13) + "\t\t4G Data attacks")
    print("3) SIP".rjust(8) + "\t\t4G IMS attacks")

    print("\nor quit to exit SigPloit\n".rjust(28))

    choice = input("\033[34msig\033[0m\033[37m>\033[0m ")

    if choice == "0":
        os.system('clear')
        # ss7main.attacksMenu()  # Uncomment this when ss7main is defined
    elif choice == "1":
        os.system('clear')
        # prep()  # Uncomment this when prep() is defined
    elif choice == "2":
        print("\n\033[34m[*]\033[0mDiameter will be updated in version 3 release..")
        print("\033[34m[*]\033[0mGoing back to Main Menu")
        time.sleep(2)
        mainMenu()
    elif choice == "3":
        print("\n\033[34m[*]\033[0mSIP will be updated in version 4 release..")
        print("\033[34m[*]\033[0mGoing back to Main Menu")
        time.sleep(2)
        mainMenu()
    elif choice == "quit" or choice == "exit":
        print('\nYou are now exiting SigPloit...')
        time.sleep(1)
        sys.exit(0)
    else:
        print('\n\033[31m[-]Error:\033[0m Please Enter a Valid Choice (0 - 3)')
        time.sleep(2)
        mainMenu()

def signal_handler(signal, frame):
    print('\nYou are now exiting SigPloit...')
    time.sleep(1)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    mainMenu()

if __name__ == '__sigploit__':
    # ss7tracking()  # Uncomment these when the functions are defined
    # ss7interception()
    # ss7fraud()
    # ss7dos()
    # attacksMenu()
    # prep()
    # gtpattacksv2()
    # gtpinfo()
    # mainMenu()
