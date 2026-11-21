import time
import sys
def print_with_delay (text ,delay =0.01 ):
    for char in text :
        sys .stdout .write (char )
        sys .stdout .flush ()
        time .sleep (delay )
    print ()
def main ():
    import os
    os .system ('cls'if os .name =='nt'else 'clear')
    banner ="""\033[96м\033[1м ██╗ ███████╗ ██████╗ ███████╗███╗ ██╗██████╗ ██████╗
    ██║ ██╔════╝██╔════╝ ██╔════╝████╗ ██║██╔══██╗██╔══██╗
    ██║ ██████╗ ██║ ███╗█████╗ ██╔██╗ ██║██║ ██║███████║
    ██║ ██╔══╝ ██║ ██║██╔══╝ ██║╚██╗██║██║ ██║██╔══██║
    ████████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝██║ ██║
    ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝ ╚═══╝╚═════╝ ╚═╝ ╚═╝\033[0m"""
    info_line ="\033[93m"+"="*70 +"\033[0m"
    contacts ="""    \033[92m📱 Телеграмма: \033[97m@FitoDomik
        \033[92m🐙 GitHub: \033[97mhttps://github.com/Legenda658"""
    bottom_line ="\033[93m"+"="*70 +"\033[0m"
    print (banner )
    print (info_line )
    print_with_delay (contacts ,0.03 )
    print (bottom_line )
if __name__ =="__main__":
    main ()