try:
    import pyfiglet
    import subprocess
    import os
    import re
    from colorama import *
    import platform
    import time
    from os import system, name
    import sys
    import pyarmor
    from progress.spinner import Spinner
except ImportError:
    print(Fore.RED + "Please wait, installing modules...")
    os.system('pip install pyinstaller')
    os.system('pip install pyarmor')
    os.system('pip install colorama')
    os.system('pip install pyfiglet')
    os.system('cls')

banner = pyfiglet.figlet_format('ObFile')
print(banner)
init()
print(Fore.GREEN + "[=] Instant Devs Corp. 2020")
print(Fore.GREEN + '[=] Obfile is a python obfuscator and compiler')
print(Fore.RED +   '----------------------------------------------')
print(Fore.GREEN + '[=] App Version : 1.1.0')
print(Fore.RED + 'User System Details')
print(Fore.GREEN + 'OS Detected : ' + platform.system())
print(Fore.GREEN + 'OS Version  : ' + platform.release())
print(Fore.RED + '------------------------------------------------')
print(Fore.GREEN + 'Developer : Kavin Jindal')
print(Fore.GREEN + 'Dev Contact : kavinsjindal@gmail.com')
print(Style.RESET_ALL)
print(' ')
print(' ')
input(Fore.RED + "Press enter to start Menu")



os.system('cls')

ascii_banner = pyfiglet.figlet_format("ObFile Menu")
print(ascii_banner)
 
while True:

    def user_choice_menu():
        while True:
            init()
            print(Fore.GREEN + ' >> Main Menu ')
            print(' ')
            print(Fore.CYAN + '    [=] Compile into exe = Type use 1')
            print(' ')
            print(Fore.CYAN + '    [=] Obfuscate File = Type use 2')
            print(' ')
            print(Fore.CYAN + '    [=] Obfuscate and compile together = Type use 3')
            print(' ')
            print(Fore.CYAN + '    [=] Help = Type use 4')
            print(' ')
            print(Fore.CYAN + '    [=] Quit Program = Type use 5')
            print(' ')
            user_input = input('>>> : ')
            
                      
                        
            if 'use 1' in user_input:
                print(Fore.GREEN + "Opening Compiler please wait")
                time.sleep(1)
                os.system('cls')
                banner = pyfiglet.figlet_format('ObFile Compiler')
                print(banner)
                print(Fore.WHITE + '---------------------------------------------------') 
                print(Fore.RED +   'ObFile Python to EXE compiler')
                print(Fore.WHITE + '---------------------------------------------------') 
                print(Fore.RED +   'You can compile your .py file into .exe with icon')
                print(Fore.RED +   'You can even compile the file without icon')
                print(Fore.RED +   'Only .ico files are allowed for icons')
                print(Fore.WHITE + '---------------------------------------------------') 
                
                print(Fore.RED + '>> Compiler Menu')
                print(Fore.CYAN + '\t[1]Compile file with custom icon = Type use 1 ')
                print(' ')
                print(Fore.CYAN + '\t[2]Compile file without icon = Type use 2')
                print(' ')
                print(Fore.CYAN + '\t[3]Quit Program = Type use 3')
                print(' ')
                user_input_1 = input('\n Type here >>')
              
                if 'use 1' in user_input_1:
                    print(Fore.CYAN + '\nThe file will be compiled into exe with custom icon')
                    dir_input = input(Fore.YELLOW + "\n Enter correct directory of file >>")
                    print(' ')
                    time.sleep(2)
                    print(Fore.CYAN + 'File Directory >> ' + dir_input)
                    print(' ')
                    icon_input = input(Fore.YELLOW + 'Enter icon directory (only .ico) >>> ')
                    print(' ')
                    time.sleep(2)
                    print(Fore.CYAN + 'Icon Directory >> ' + icon_input)
                    print(' ')
                    print(Fore.YELLOW + 'Starting compiling process')
                    time.sleep(2)
                    os.system(f'pyinstaller -F -i "{icon_input}" {dir_input}')
                    os.system('clear')
                    print(Fore.RED + '\n\tCompiling process finished')
                
                if 'use 2' in user_input_1:
                    print(Fore.CYAN + '\n The file will compile into exe without a custom icon')
                    dir2_input = input(Fore.YELLOW + "\n Enter correct directory of file >>")
                    time.sleep(1)
                    print(Fore.CYAN + '\nFile Directory >> ' + dir2_input)
                    time.sleep(1)
                    print(Fore.YELLOW + 'Starting compiling process')
                    time.sleep(2)
                    os.system(f'pyinstaller -F  {dir2_input}')
                    os.system('clear')
                    print(Fore.RED + '\n\tCompiling process finished')

                if 'use 3' in user_input_1:
                    print(Fore.RED + '\n Quitting program.....')
                    time.sleep(1)
                    print(Fore.CYAN + '\n Sorry to see you go :(')
                    sys.exit(2)

                else:
                    input(Fore.CYAN + 'Press enter to continue')
                    os.system('cls')
             
    
            
            if 'use 2' in user_input:
                print(Fore.GREEN + "Opening Obfuscator")
                time.sleep(1)
                os.system('cls')
                banner1 = pyfiglet.figlet_format('ObFile Obfuscator')
                print(banner1)

                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'ObFile Obfuscator')
                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'You can only "Obfuscate your python file with this tool"')
                print(Fore.RED +   'Make sure to enter the correct file path')
                print(Fore.WHITE + '--------------------------------------------------------') 
                input(Fore.RED +   "Press to Continue >>")


                ob_dir = input(Fore.RED + "\n [=] Enter the file directory>> ")
                print(Fore.WHITE + '\n Starting Compiling....')
                os.system(f'pyarmor obfuscate {ob_dir}')
                print(Fore.WHITE + "Obfuscation Complete")
                input(Fore.RED + "Press to continue")           
                
            
            
            if 'use 3' in user_input:
                print('Running program, please wait...')
                time.sleep(1)
                os.system('cls')
                banner2 = pyfiglet.figlet_format('Obfile')
                print(banner2)

                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'ObFile Obfuscator and Compiler')
                print(Fore.WHITE + '--------------------------------------------------------') 
                print(Fore.RED +   'You can obfuscate your python file and also compile it to exe with this tool')
                print(Fore.RED +   'You can also add icons to your file (only .ico files are allowed)')
                print(Fore.RED +   'Make sure to enter the correct file path and icon path')
                print(Fore.WHITE + '--------------------------------------------------------') 
                input(Fore.RED +   "Press to Continue >>") 

                print(Fore.YELLOW + "Menu >> ")
                print(Fore.WHITE + "\t\n [=] Add icon Type use 1")
                print(Fore.WHITE + '\t\n [=] Compile Without icon Type use 2')
                user_input3 = input(Fore.RED + "Type here >>")

                if 'use 1' in user_input3:
                    print(Fore.YELLOW + "The program will compile with an icon")
                    com_dir = input(Fore.RED + '\n [=] Enter File directory >>')
                    print(Fore.WHITE + f'\n\t File directory >> {com_dir}')
                    icon_dir = input(Fore.RED + '\n [=] Enter icon directory >>')
                    print(Fore.WHITE + f'\n\t Icon Directory >> {icon_dir}')
                    print(Fore.YELLOW + "Processing.....")
                    time.sleep(1)
                    print(Fore.YELLOW + "Process started")
                    os.system(f'pyarmor pack -e "--onefile --noconsole --icon {icon_dir}" {com_dir}' )
                    print(Fore.RED + 'Processing done.....')

                if 'use 2' in user_input3:
                    print(Fore.YELLOW + "The file will compile without icon")
                    com_dir1 = input(Fore.RED + "\n [=] enter file directory >>")
                    print(Fore.WHITE + f'\n\t File directory >> {com_dir1}')
                    print(Fore.YELLOW + 'Processing.....')
                    os.system(f'pyarmor pack -e " --onefile --noconsole" {com_dir1}')
                    print(Fore.RED + "Processed.....")
                
             
               

            if 'use 4' in user_input:
                os.system('HELP.txt')
            
            if 'use 5' in user_input:
                print("Quitting")
                time.sleep(2)
                sys.exit(2)
            
            else:
                input(Fore.CYAN + 'Press enter to continue')
                os.system('cls') 
    user_choice_menu()






#os.system(f'pyarmor obfuscate {directory}')
#os.system(f'pyinstaller -F -i "{icon}" {directory}')
