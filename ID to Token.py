# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.YELLOW+ """
 _______  _       _                _               _      _ 
(_____  )( )  _  ( )              ( )             (_)    ( )
     /'/'| | ( ) | |   __     __  | |/')   ___    | |   _| |
   /'/'  | | | | | | /'__`\ /'__`\| , <  /',__)   | | /'_` |
 /'/'___ | (_/ \_) |(  ___/(  ___/| |\`\ \__, \   | |( (_| |
(_______)`\___x___/'`\____)`\____)(_) (_)(____/   (_)`\__,_)
                                                            
                                                                             
MADE BY ZeDeen""" + Fore.LIGHTRED_EX)
print(banner)
userid = input(" Root@ZeDeen/ ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n Root@ZeDeen/TOKEN FIRST PART : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
