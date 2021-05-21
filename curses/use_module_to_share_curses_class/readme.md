run
python3 main.py

This test is built upon the knowledge that we can initialize class with curses object. (wrapper_curses_in_class)
If system works correctly, we should see that we can access the same curses object from 2 different modules.
We should see the window object with the same address.

<_curses.curses window object at 0x7f2c6795d1d0>
<_curses.curses window object at 0x7f2c6795d1d0>