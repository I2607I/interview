import webbrowser
from pynput.keyboard import Key, Controller
import time
import sys
import os

import settings as sts

dict_time = {'tech': [sts.tech_time], 'algo': [sts.algo_time], 'interview': [sts.interview_tech_time, sts.interview_algo_time]}
dict_number = {'tech': [sts.tech_number], 'algo': [sts.algo_number], 'interview': [sts.interview_tech_number, sts.interview_algo_number]}


time_start = time.time()
seconds = 0
minutes = 0
flag_start = False
while True:
    try:
        if flag_start is False:
            a = input(">>> ")
            if a == 'algo':
                # алгоритмический собес
                webbrowser.open("input.py")
                flag_start = True
            elif a == 'tech':
                # технический собес
                webbrowser.open("input.py")
                flag_start = True
            elif a == 'interview':
                # полный собес
                webbrowser.open("input.py")
                flag_start = True
            elif a == 'exit':
                break
            if flag_start:
                    print(zip(dict_time[a],dict_number[a]))
                    minutes = sum([i*j for i,j in zip(dict_time[a],dict_number[a])])
        if flag_start is True:
            os.system('clear')
            sys.stdout.write(f"The {a} interview is on!\n")
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
            # sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
            if seconds <= 0:
                minutes -= 1
                seconds = 60
        
    except KeyboardInterrupt as e:
        break