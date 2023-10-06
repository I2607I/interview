import webbrowser
from pynput.keyboard import Key, Controller

import time
import sys
time_start = time.time()
seconds = 0
minutes = 0
flag = False
while True:
    try:
        if flag is False:
            a = input(">>> ")
            if a == 'start algo':
                # алгоритмический собес
                webbrowser.open("input.py")
                flag = True
            elif a == 'start tech':
                # технический собес
                webbrowser.open("input.py")
                flag = True
            elif a == 'start interview':
                # полный собес
                webbrowser.open("input.py")
                flag = True
            elif a == 'exit':
                break
        if flag is True:
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
        
    except KeyboardInterrupt as e:
        break