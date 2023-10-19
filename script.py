from bs4 import BeautifulSoup
import requests
import pandas as pd
import time, sched
from tkinter import *
from tkinter import messagebox

#Input links of courses
links = [
    'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in=202308&crn_in=81574',
    'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in=202308&crn_in=82833',
    'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in=202308&crn_in=84247'
]


#Setting repeated auto-fetch
s = sched.scheduler(time.time, time.sleep)

print(" ")
print("#########################################################")
print(" ")

#Fetching each course
def runOnClass(link):
    html_txt = requests.get(link).text
    soup = BeautifulSoup(html_txt, 'lxml')

    #Get name of course
    className = soup.find(class_ = "ddlabel")
    className = str(className)[32:-15]

    #Get Availability values
    dddefault = soup.find_all(class_ = "dddefault") 

    #Setting table view
    table = [[],[]]
    for i in range(1, len(dddefault)):
        index = (i - 1) // 3
        table[index].append(str(dddefault[i])[22:][:-5])
    df = pd.DataFrame(table, columns = ['Capacity', 'Actual', 'Remaining'], index=['Seats', 'Waitlist'])
    
    #Print Table
    
    print(className)
    print(df)
    print(" ")
    
    #Pop-up if if "Remaining" changes
    #seats_remaining = int(table[0][2])
    seats_capacity = int(table[0][0])
    seats_actual = int(table[0][1])
    #waitList_remaining = int(table[1][2])
    #waitList_remaining = 0

    if (seats_capacity > seats_actual):
        print(className)
        print(df)
        print(" ")

        root = Tk()
        messagebox.showinfo("Hi")
        root.mainloop()
        

    # if ((seats_remaining != 0) or (waitList_remaining != 0)):
    #     print(className)
    #     print(df)
    #     print(" ")

    #     root = Tk()
    #     messagebox.showinfo("Hi")
    #     root.mainloop()
    

#Full Script
def script(sc):

    for link in links:
        runOnClass(link)

    '''
    print(" ")
    print("#########################################################")
    print(" ")
    '''

    sc.enter(1, 1, script, (s,))

try: 
    s.enter(1, 1, script, (s,))
    s.run()
except:
    print("Too many tries")


