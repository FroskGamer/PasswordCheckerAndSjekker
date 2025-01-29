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
        


    def repetitive_letter(passwordinput, score):
        remove_with = 0
        i = 0


        passwordinputRL = ''.join([char for char in passwordinput if char.isalnum()])

        while i < len(passwordinputRL) - 1:
            if passwordinputRL[i] == passwordinputRL[i + 1]:
                remove_with += 1
                i += 2
            else:
                i += 1
        
        if remove_with > 1:

            score -= remove_with * 2
            print(f"Found repeated letters/symbols in {passwordinput} | -{remove_with * 2}")
        else:
            print("Repetitive characters: Check")
        return score

    def repetitive_special_character(passwordinput, score):
        remove_with = 0
        i = 0


        passwordinputRSC = ''.join([char for char in passwordinput if not char.isalnum()])

        while i < len(passwordinputRSC) - 1:
            if passwordinputRSC[i] == passwordinputRSC[i + 1]:
                remove_with += 1
                i += 2
            else:
                i += 1


        if remove_with > 1:
            score -= remove_with * 5
            print(f"Found repeated special characters in {passwordinput} | -{remove_with * 5}")
        else:
            print("Repetetive Special characters: Check")
        return score

    #koble checker med generator










    listcharacters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
        "u", "v", "w", "x", "y", "z", "æ", "ø", "å", 
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z", "Æ", "Ø", "Å"
        ]
    listnumbers = [
        "1", "2", "3", 
        "4", "5", "6", 
        "7", "8", "9"
        ]



    password = ""

    amountcharacter = random.randint(16, 24)
    amountnumber = random.randint(3, 6)

    for i in range(amountcharacter):
        letter = random.choice(listcharacters)
        
        password += letter

    for i in range(amountnumber):
        digit = random.choice(listnumbers)

        password += digit




    #TEST PASSORD
    #password = "aaAAååÅÅiiII11jjJJppPPggGG88"   
    #print(password)

    def upgrade_password(password):
        upgraded_password = ""

        for char in password:

            if char.lower() == "a" or char.lower() == "å" or char == "2": 
                replace = random.randint(1,3)
                if replace > 1:
                    char = "@"

            if char.lower() == "i" or char == "1" or char == "4":
                replace = random.randint(1,3)
                if replace > 1:
                    char = "!"

            if char.lower() == "j" or char.lower() == "p" or char == "6":
                replace = random.randint(1,3)
                if replace > 1:
                    char = "?"
            
            if char.lower() == "g" or char == "8" or char == "9":
                replace = random.randint(1,3)
                if replace > 1:
                    char = "#"
                
            if char == "3" or char == "5" or char == "7":
                replace = random.randint(1,3)
                if replace == 2:
                    char = "%"
                if replace == 3:
                    char = "&"

            upgraded_password += char
        return upgraded_password

    upgraded_password = upgrade_password(password)



    passwordinput = upgraded_password

    #ferdig resultater
    print(f"Your randomly generated password is {passwordinput}")
    print("------------------------")
    score = password_length(passwordinput)
    score = spesiell_karakter(passwordinput, special_character, score)
    score = number(passwordinput, score)
    score = caps_letters(passwordinput, score)
    score = small_letters(passwordinput, score)
    print("------------------------")
    score = word_in_password(passwordinput, score)
    score = repetitive_letter(passwordinput, score)
    score = repetitive_special_character(passwordinput, score)
    print("------------------------")
    score = round(score, 2)

    if score <= 0:

        score = str(score).replace(".", ",") 
        print(f"Your score is {score}/100")
        print("In other words, it's shit")

    else: 
        #komma er best
        score = str(score).replace(".", ",") 
        print(f"Your score is {score}/100")