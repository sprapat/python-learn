from curses import wrapper

class Display:
    def __init__(self, stdscr):
        print("Display init")
        self.stdscr = stdscr

# wrapper will call Display with curses objects as parameter
# So we should be able to initialize the class as shown in the Display class
display = wrapper(Display)
