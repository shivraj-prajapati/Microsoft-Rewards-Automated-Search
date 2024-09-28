import random
import pyautogui as rocky
import time
from questions import question
time.sleep(2)

def open_edge_with_run_command():
    
    rocky.hotkey('win', 'r')
    time.sleep(1)  

    rocky.typewrite('msedge')
    time.sleep(1)  
        
    rocky.press('enter')
    time.sleep(3)  

open_edge_with_run_command()

#todo Uncomment if you have multiple accounts

# # First Account
# rocky.click(30,16,clicks=1)
# time.sleep(1)
# rocky.click(166,360,clicks=1)

# # Second Account 
# rocky.click(30,16,clicks=1)
# time.sleep(1) 
# rocky.click(125,413,clicks=1)
    
# # Third Account 
# rocky.click(30,16,clicks=1)
# time.sleep(1)
# rocky.click(143,441,clicks=1)

time.sleep(1)
def google_search(query):
    rocky.typewrite(query, interval=0.04) #Increase typing speed in Searching time {slow = 1 , fast = 0.02}
    rocky.press('enter')
    time.sleep(random.uniform(1,4))  

def close_edge():    
    rocky.hotkey('alt', 'f4')
    time.sleep(1)  

random_questions = random.sample(question, 40)

for query in random_questions:
    google_search(" " + query)
    time.sleep(3) 

if __name__ == "__main__":
    close_edge()