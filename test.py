import random
import time as tm


repeat = 0
while repeat < 30:
    repeat += 1
    tm.sleep(2)
    
    #25 max poeng for 15+ karakterer
    def password_length(passwordinput, length=15, score=0): 
        

        #isalpha sjekker etter karakterer som er bokstaver. join putter elementer sammen i et element, "" er hva som skal mellom elementene
        alphapassword = "".join(char for char in passwordinput if char.isalpha())

        #1,8 poeng hver karakter
        score = len(alphapassword) * 1.5
        if len(alphapassword) >= length:
            score = 25
            print(f"Length: Check | +{score}")
            
        
        elif len(alphapassword) < length:
            short_by = length - len(alphapassword)
            print(f"Your password is {short_by} character(s) too short. | +{score}")
        
        return score




    #20 max poeng for 4+ spesiell karakterer.
    def spesiell_karakter(passwordinput, special_character, score):
        short_by = 4
        special_amount = 0
        
        
        for char in passwordinput:
            if char in special_character:
                short_by -= 1
                special_amount += 1

        #20 poeng hvis 4 eller flere spesiell karakterer  
        if special_amount >= 4:
            special_amount = 20
            score += special_amount
            print(f"Special character: Check | +{special_amount}")
        
        
        #3,75 poeng hver spesiell karakter
        elif special_amount < 4:
            special_amount *= 3.75
            score += special_amount
            print(f"Your password is {short_by} special character(s) too short. | +{special_amount}")
        return score
    special_character = "!#¤%&/()=?@£$[]{}+-.,-_"
        
    #20 max poeng
    def number(passwordinput, score, tall = 5):
        short_by = 5

        antalltall = sum(1 for char in passwordinput if char.isdigit())
        
        #20 poeng hvis 5+ tall
        if antalltall >= tall:
            score += 20
            print("Numbers: Check | +20")
            
        
        #4,2 poeng hvert tall
        elif antalltall < tall:
            short_by -= antalltall
            
            add_with = antalltall * 4.2
            add_with= round(add_with, 2)
            score += antalltall * 4.2
            print(f"Your password is {short_by} numbers too short. | +{add_with}")
        
        return score
        
    #20 max poeng
    def caps_letters(passwordinput, score):
        caps_amount = 0
        short_by = 4
        
        for char in passwordinput:
            if char.isupper():
                caps_amount += 1
                short_by -= 1
        
        if caps_amount >= 4:
            score += 20
            print(f"Capitalization: Check | +20")
            
        
        elif caps_amount < 4:
            add_with = caps_amount * 3.75
            score += caps_amount * 3.75

            print(f"Your password is {short_by} capitalized letter(s) too short. | +{add_with}")
        
        return score


    #15 max score
    def small_letters(passwordinput, score):
        small_amount = 0
        password_amount = "".join(char for char in passwordinput if char.isalpha())
        short_by = len(password_amount)/2

        for char in passwordinput:
            if char.islower():
                short_by -= 1
                small_amount +=1
            if short_by < 0:
                short_by = 0
        
        #15 score hvis halvparten av bokstavene er små
        if small_amount >= short_by:


            score += 15
            print("Small: Check | +15")
            
        #1 score hver liten bokstav
        elif small_amount < 15:
            if small_amount < short_by:

                score += small_amount * 1
                print(f"Your password is {short_by} small letters too short. | {small_amount}")
                
        else:
            score += 10
            print("No idea how you managed this. | +10")


        return score


    #fjerner poeng 
    def word_in_password(passwordinput, score):

        if 'passord' in passwordinput:
            score -= 20
            print(f"Found passord in {passwordinput} | -20")

        elif 'password' in passwordinput:
            score -20
            print(f"Found password in {passwordinput} | -20")
        
        else: 
            print("Often used words: Check")

            
        
        if '123' in passwordinput:
            score -=15
            print(f"Found 123 in {passwordinput} | -15")
        

        else:
            print("Often used numbers: Check")
        return score
        


