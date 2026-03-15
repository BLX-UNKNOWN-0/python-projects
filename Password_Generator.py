# BLX-UNKNOWN-0
# PROJECT 4 // PASSWORD-GENERATOR
# Learned: import, random, while loops, strings

import string
import random

def password ():
    print("... PASSWORD-GENERATOR...")
    
    while True:
        try:
            pass_Len = int(input("Enter your password length "))
            
        except ValueError:
            print("Enter valid numbers!")
            continue 

        strongness_lvl= int(input("Choose how strong password you want as lvl \n 1.(simple) \n 2.(medium)\n 3.(Strongest)" ))
        if strongness_lvl ==1:
            all_chars = string.ascii_letters 
        elif strongness_lvl == 2:
            all_chars = string.ascii_letters + string.digits 
        elif strongness_lvl == 3 :
            all_chars = string.ascii_letters + string.digits + string.punctuation
        else :
            print("Invalid Number, choose between / 1-3")
            continue
        key = []
        for i in range (pass_Len):
            key.append (random.choice(all_chars))
        
        random.shuffle(key)
        password = "" .join(key)
        
        
        print("your pasword = " , password)
password()