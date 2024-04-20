from datetime import datetime
import time 
import os
from colorama import Fore, init

init()

ascii = """

  █████▒    ██▀███      ▄▄▄▄   
▓██   ▒    ▓██ ▒ ██▒   ▓█████▄ 
▒████ ░    ▓██ ░▄█ ▒   ▒██▒ ▄██
░▓█▒  ░    ▒██▀▀█▄     ▒██░█▀  
░▒█░       ░██▓ ▒██▒   ░▓█  ▀█▓
 ▒ ░       ░ ▒▓ ░▒▓░   ░▒▓███▀▒
 ░           ░▒ ░ ▒░   ▒░▒   ░ 
 ░ ░         ░░   ░     ░    ░ 
              ░         ░      
                             ░ 
       ░  
Fake    Roblox   Ban
"""

print(Fore.LIGHTRED_EX + ascii)
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

with open('template.html', 'r') as f:
    html = f.read()

html = html.replace('/set name here/', input('Display name: '))
try:
    verified = input('Do you want to be verified? (y/n): ')
    if verified == 'y':
        html = html.replace('data-hasverifiedbadge="true"', 'data-hasverifiedbadge="true"')
    else:
        html = html.replace('data-hasverifiedbadge="true"', 'data-hasverifiedbadge="false"')
except:
  print("select a valid option. idiot.")
  time.sleep(2)
  exit()
date_obj = datetime.now()
date_str = date_obj.strftime('%m/%d/%Y %I:%M:%S %p (CT)')
html = html.replace('/set date here/', date_str)

html = html.replace('/set message here/', input('Moderator Note: '))
html = html.replace('/set reason here/', input('Reason: '))
html = html.replace('/set proof here/', input('Offensive Item: '))

with open('dist/creation.html', 'w') as f:
    f.write(html)
