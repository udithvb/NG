#type reset
import os
import curses
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
                                                                              


with open('s1') as file:
    lines = ' '.join([line.rstrip('\n') for line in file])
    name = file.name

splitLines = lines.split(". ")
 
#def teardown(): #taken care of by wrapper
#    curses.nocbreak()
#    stdscr.keypad(False)
#    curses.echo()
#    curses.endwin()
#ne = True
#def quitCurses(stdscr):
#    curses.endwin()
#    stdscr.addstr(f"Quitting")
#    time.sleep(0.5)
#    ne = False
    
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
#    c = stdscr.getch()
##    stdscr.clear()
##    if c == 27:
##        curses.addstr("yo esc")
##
#def main(stdscr):
#    # Make stdscr.getch non-blocking
#    stdscr.nodelay(True)
#    stdscr.clear()
#    width = 4
#    count = 0
#    direction = 1
#    while True:
#        c = stdscr.getch()
#        # Clear out anything else the user has typed in
#        curses.flushinp()
#        stdscr.clear()
#        # If the user presses p, increase the width of the springy bar
#        if c == ord('p'):
#            width += 1
#        # Draw a springy bar
#        stdscr.addstr("#" * count)
#        count += direction
#        if count == width:
#            direction = -1
#        elif count == 0:
#            direction = 1
#        # Wait 1/10 of a second. Read below to learn about how to avoid
#        # problems with using time.sleep with getch!
#        time.sleep(0.1)



#if __name__ == ' __main__':
wrapper(main)
