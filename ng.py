#type reset
from sys import argv
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
script,filename = argv
                                                                              


with open(filename) as file:
    lines = ' '.join([line.rstrip('\n') for line in file])
    name = file.name

splitLines = lines.split(". ")
start = time.time()
end = 0
log_list = list()

for i in range(len(splitLines)):
    log_list.append(" ")

stdscr.addstr(1,24,"██╗   ██╗██████╗     ██╗███╗   ██╗ ██████╗   ")
stdscr.addstr(2,24,"██║   ██║██╔══██╗    ██║████╗  ██║██╔════╝   ")
stdscr.addstr(3,24,"██║   ██║██████╔╝    ██║██╔██╗ ██║██║        ")
stdscr.addstr(4,24,"╚██╗ ██╔╝██╔══██╗    ██║██║╚██╗██║██║        ")
stdscr.addstr(5,24," ╚████╔╝ ██████╔╝    ██║██║ ╚████║╚██████╗██╗")
stdscr.addstr(6,24,"  ╚═══╝  ╚═════╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝")
stdscr.addstr(7,24,f"{len(splitLines)}")
stdscr.addstr(8,24,str(type(splitLines)))
stdscr.addstr(9,24,str(len(splitLines)))


    

def main(stdscr,splitLines=splitLines,y=y,x=x):
    global log_list
    global end
    lineNumber = 0
    prev = time.time()
    while True:
        curses.flushinp()

        # Store the key value in the variable `c`
        c = stdscr.getch()
        # Clear the terminal
        stdscr.clear()
        if c== ord('q') or c == 27 or c == ord('Q'):
            end = abs(start - time.time())
            break
        elif c == ord('j') or c == ord('l'): #or c == KEY_RIGHT:
            lineNumber += 1 #next line
            try:
                log_list[lineNumber] = abs(prev - time.time()) #index error
            except:
                break
            prev = time.time()
            stdscr.addstr(int(y/2),4,splitLines[lineNumber] + ".")
            
        elif c == ord('k') or c == ord('h'):
            lineNumber -= 1 #prev line
            stdscr.addstr(int(y/2),4,splitLines[lineNumber] + ".")
        else:
            stdscr.addstr("Not Mapped!")
            
#            pass
#if __name__ == ' __main__':
wrapper(main)

try:
    open(f"log_{filename}",'x')
except FileExistsError:
    print(f"appending to existing file!\n---> log_{filename}")

#this dosent print last line time
with open(f"log_{filename}",'a') as logfile:
    for i in range(len(log_list)):
        logfile.write(str(log_list[i]) + "\n")

    logfile.write(str(end) + "\n")
    logfile.write("********************")
    print("done.")
