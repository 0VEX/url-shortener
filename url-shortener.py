# url-shortener
# ---------------------------------------------------------------------------------------------------------

# Libraries

import os
import webbrowser
import pyshorteners
from colorama import Fore , init 
import time

# Colors
init(autoreset=True)
m = Fore.MAGENTA
b = Fore.BLUE 
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
g = Fore.GREEN
w = Fore.WHITE
bl = Fore.BLACK
#---------------------------
lm = Fore.LIGHTMAGENTA_EX
lb = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX
ly = Fore.LIGHTYELLOW_EX
lc = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lw = Fore.LIGHTWHITE_EX
lbl = Fore.LIGHTBLACK_EX

# More

red = "\033[1;31;40m";yel = '\033[1;33;40m'
bloFT = "\033[1;36;40m"
grn = '\033[1;32;40m';wit = "\033[1;37;40m"

# ---------------------------------------------------------------------------------------------------------

os.system('cls')

# the king
def logo():
 print(f"""
      {b}██{r}╗   {b}██{r}╗    {b}███████{r}╗    {b}██{r}╗  {b}██{r}╗
      {b}██{r}║   {b}██{r}║    {b}██{r}╔════╝    {r}╚{b}██{r}╗{b}██{r}╔╝
      {b}██{r}║   {b}██{r}║    {b}█████{r}╗       {r}╚{b}███{r}╔╝ 
      {r}╚{b}██{r}╗ {b}██{r}╔╝    {b}██{r}╔══╝       {b}██{r}╔{b}██{r}╗ 
       {r}╚{b}████{r}╔╝     {b}███████{r}╗    {b}██{r}╔╝ {b}██{r}╗
        {r}╚═══╝      ╚══════╝    ╚═╝  ╚═╝
            https://github.com/0VEX                                         
                                """)
logo()
while True:

 # asks the user to input the link so the tool can short it

 link = input(f"{r}[/]{b}Enter the link (google.com) --> ")

 if link == "":
    print()
    print(f"{r}[!]{b}invalid option .")
    print()
    link = input(f"{r}[/]{b}Enter the link (google.com) --> ")


 # using the shorteners laibrary

 shortener=pyshorteners.Shortener()

 # getting request from tinyurl.com and the x means the link

 x = shortener.tinyurl.short(f'https://{link}')
 print()

 # the link

 print(f"{r}[+]{b}Here is your link : " +r+(x))
 print()

 print(f"{r}[+]{b}Done shorting the link")
 print()
 
 webbrowser.open(f'{x}')

 again = input(f"{r}[?]{b}Do you want to short another link (y/n) --> ")
 if again == "y" or again == "Y":
     os.system('cls')
     logo()

 elif again == "n" or again == "N":
     print()
     print(f"{r}[-]{b}Thanks for using the tool !")
     exit()
 
 else :
    print()
    print(f"{r}[!]{b}invalid option .")
    time.sleep(3)
    os.system('cls')
    logo()

