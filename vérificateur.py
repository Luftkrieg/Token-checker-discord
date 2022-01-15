import requests
from colorama import *
import time

a = 1
c = 2
b = 0
while a < c:
    file = open('token.txt', "r")
    pass1 = file.readlines()
    data = pass1[b].replace('\n', '')
    token = data
    headers = {
        'Authorization': token
    }
    login = requests.get(
        'https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)	
            f = open('valids.txt', "a+")
            f.write(f'{data}\n')
            b += 1
        elif login.status_code == 429:
            print('temps de pause de 10 secondes')
            time.sleep(10.0)
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
            time.sleep(1.0)
            b += 1
    finally:
        print("")