# password must contain
# Minstens 8 karakters
# Minstens 1 hoofd- en kleine letter
# Minstens 1 cijfer

import re

def main():
    username = input("Username: ")
    password = input("Password: ")

    result = bool(re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", password))

    if result:
        print("Goed passwoord")
    else:
        print("passwoord fout loser")

main()