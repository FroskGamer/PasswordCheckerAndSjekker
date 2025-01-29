import random




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


#TEST REPEAT
repeat = 0
while repeat < 10:

    password = ""

    repeat += 1

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

    print(upgraded_password)