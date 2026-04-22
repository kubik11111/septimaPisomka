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


dir = os.path.dirname(__file__)                     # Nacita cestu k suboru
with open(dir + "/passwords.txt", 'r') as file:     # Otvori subor s heslami
    for password in file:                           # Prejde vsetky riadky/hesla
        if check_password(password):                # Skontroluje ich
            print(password, end = "")
