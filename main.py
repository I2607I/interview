import webbrowser
import subprocess
from pynput.keyboard import Key, Controller
import time
import sys
import os
import random
import os, random

import settings as sts

dict_time = {'tech': [sts.tech_time, 0], 'algo': [0, sts.algo_time], 'interview': [sts.interview_tech_time, sts.interview_algo_time]}
dict_number = {'tech': [sts.tech_number, 0], 'algo': [0, sts.algo_number], 'interview': [sts.interview_tech_number, sts.interview_algo_number]}
example = ['first', 'second']
ex = random.choice(example)
print(ex)

def find_problem(type_interview):
    count_questions = dict_number[type_interview][0]
    count_problems = dict_number[type_interview][1]
    questions = []
    problems = []
    files_list = random.sample(os.listdir("algo_problems"), k=count_problems)
    for filename in files_list:
        filename = "algo_problems/" + filename
        with open(filename) as file:
            problem = file.read()
            problems.append(problem)
    return problems

print(find_problem("algo"))
time_start = time.time()
seconds = 60
minutes = 0
flag_start = False
while True:
    try:
        if flag_start is False:
            a = input(">>> ")
            if a == 'algo':
                # алгоритмический собес
                # webbrowser.open("input.py")
                flag_start = True
            elif a == 'tech':
                # технический собес
                # webbrowser.open("input.py")
                flag_start = True
            elif a == 'interview':
                # полный собес
                # webbrowser.open("input.py")
                flag_start = True
            elif a == 'exit':
                break
            if flag_start:
                    print(zip(dict_time[a],dict_number[a]))
                    minutes = [i*j for i,j in zip(dict_time[a],dict_number[a])]
                    all_minutes = sum(minutes)
                    questions = sum(dict_number[a])
                    times = sum(dict_time[a])
                    all_minutes -= 1
                    problems = find_problem(a)
        while True:
            if flag_start is True:
                os.system('clear')
                sys.stdout.write(f"The {a} interview is on!\n")
                for i, (t, n) in enumerate(zip(dict_time[a],dict_number[a])):
                    if t != 0:
                        if i == 0:
                            sys.stdout.write(f"Questions tech left: {int((all_minutes+1-minutes[1])/t)}\n")
                        else:
                            n = int((all_minutes+1)/t)
                            sys.stdout.write(f"Questions algo left: {n}\n")
                            problem = problems[n-1]
                            
                # sys.stdout.write(f"Total questions left: {all_minutes//times + 1}\n")
                sys.stdout.write(f"Total time left: {all_minutes} Minutes {seconds} Seconds\n")
                print()
                print(problem)
                time.sleep(1)
                seconds -= 1
                if all_minutes == 0 and seconds == 0:
                    flag_start = False
                    break
                if seconds <= 0:
                    all_minutes -= 1
                    seconds = 60
        print("Time left!")
        subprocess.run(["gedit", "main.py"])
            
    except KeyboardInterrupt as e:
        break