import os
from colorama import Fore , init 


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

os.system('pip install shorteners')
os.system('pip install colorama')
os.system('pip install webbrowser')
os.system('pip install time')

os.system('cls')

print(f"""
      {lc}██{lr}╗   {lc}██{lr}╗    {lc}███████{lr}╗    {lc}██{lr}╗  {lc}██{lr}╗
      {lc}██{lr}║   {lc}██{lr}║    {lc}██{lr}╔════╝    {lr}╚{lc}██{lr}╗{lc}██{lr}╔╝
      {lc}██{lr}║   {lc}██{lr}║    {lc}█████{lr}╗       {lr}╚{lc}███{lr}╔╝ 
      {lr}╚{lc}██{lr}╗ {lc}██{lr}╔╝    {lc}██{lr}╔══╝       {lc}██{lr}╔{lc}██{lr}╗ 
       {lr}╚{lc}████{lr}╔╝     {lc}███████{lr}╗    {lc}██{lr}╔╝ {lc}██{lr}╗
        {lr}╚═══╝      ╚══════╝    ╚═╝  ╚═╝
            https://github.com/0VEX                                         
                                """)


print(f"{lr}[+]{lc}Done setting up the tool you can now run it")
print()
ready = input(f"{lr}[!]{lc}Press ENTER to exit")