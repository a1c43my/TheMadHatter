from ast import For
from colorama import *
#make sure you reset at the last executed command so your terminal isnt colored :) 

def color_text():
    print('test text')

red = Fore.RED
rst = Style.RESET_ALL

blk_txt = print(Fore.BLACK + 'some black text')
wht_txt = print(Back.WHITE + 'some black text w/ white background (no reset used)')
red_text = print(Fore.RED + 'some red text (no reset used)')

err_msg = Fore.RED + 'error text (no reset used)' + rst

print(err_msg)
red = Fore.RED
print(red+'hello'+rst)
print('back to normal now (first reset used)')