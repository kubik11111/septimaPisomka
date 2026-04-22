# sem doplnte link na svoj kod

import os;

def check_password(password: str) -> bool:    
    small_letter = False
    capital_letter = False
    number = False

    for c in password:
        if(c.isdigit()):
            number = True
        elif(c.islower()):
            small_letter = True
        elif(c.isupper()):
            capital_letter = True
    
    return small_letter and capital_letter and number


dir = os.path.dirname(__file__)
with open(dir + "/passwords.txt", 'r') as file:
    for line in file:
        if check_password(line):
            print(line, end = "")
