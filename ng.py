#type reset
from sys import argv
import os
import curses
import time
from curses import wrapper
stdscr = curses.initscr()
#curses.noecho()
curses.cbreak()
stdscr.keypad(True)
y,x = stdscr.getmaxyx()
#x = int(x/2)
#y = int(y/2)
#stdscr.addstr(str(y) + " " + str(x))
stdscr.addstr(1,24,"██╗   ██╗██████╗     ██╗███╗   ██╗ ██████╗   ")
stdscr.addstr(2,24,"██║   ██║██╔══██╗    ██║████╗  ██║██╔════╝   ")
stdscr.addstr(3,24,"██║   ██║██████╔╝    ██║██╔██╗ ██║██║        ")
stdscr.addstr(4,24,"╚██╗ ██╔╝██╔══██╗    ██║██║╚██╗██║██║        ")
stdscr.addstr(5,24," ╚████╔╝ ██████╔╝    ██║██║ ╚████║╚██████╗██╗")
stdscr.addstr(6,24,"  ╚═══╝  ╚═════╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝")

script,filename = argv
                                                                              


with open(filename) as file:
    lines = ' '.join([line.rstrip('\n') for line in file])
    name = file.name

splitLines = lines.split(". ")


def main(stdscr,splitLines=splitLines,y=y,x=x):
    lineNumber = 0
    while True:
        #stdscr.move(y,x)
        curses.flushinp()

        # Store the key value in the variable `c`
        c = stdscr.getch()
        # Clear the terminal
        stdscr.clear()
        if c== ord('q') or c == 27 or c == ord('Q'):
            #stdscr.addstr(0,x,"You pressed the 'q' key.")
            #time.sleep(0.5)
            #curses.endwin()
            #stdscr.addstr(f"{curses.isendwin()}")
            break
            #ne = False
            #quitCurses()
        elif c == ord('j') or c == ord('l'): #or c == KEY_RIGHT:
            lineNumber += 1 #next line
            stdscr.addstr(int(y/2),4,splitLines[lineNumber] + ".")
            
        elif c == ord('k') or c == ord('h'):
            lineNumber -= 1 #prev line
            stdscr.addstr(int(y/2),4,splitLines[lineNumber] + ".")
        else:
            stdscr.addstr("Not Mapped!")
#if __name__ == ' __main__':
wrapper(main)
