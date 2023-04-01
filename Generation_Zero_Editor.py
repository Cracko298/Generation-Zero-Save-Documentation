from time import sleep
from os import remove
from os import system
from os import path
from os import mkdir
from glob import glob
from shutil import copy2
print("Created By: Cracko298")
sleep(2)
num = 0

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
    clear = 'cls'
else:
    clear = 'clear'

system(clear)

def SkillPoints():
    global clear
    system(clear)
    sleep(0.5)
    print(" Skill Point Editor - Version 1.0")
    print(" This Function Edits Player Skill Points.")

    number = int(input(" Number of Skill Points: "))

    byte_array = bytearray(number.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]

    with open('savegame', 'rb+') as bin_file:
        bin_file.seek(928)
        bin_file.write(reversed_array)
    
    print(f" Wrote Value of {number} to Generation Zero Save-File.")
    sleep(4)
    UserMenu()


def PlayerLevel():
    global clear
    system(clear)
    sleep(0.5)
    print(" Player Level Editor - Version 1.0")
    print(" This Function Edits The Player Level.")

    number = int(input(" Player Level: "))

    byte_array = bytearray(number.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]

    with open('savegame', 'rb+') as bin_file:
        bin_file.seek(940)
        bin_file.write(reversed_array)
    
    print(f" Wrote Value of {number} to Generation Zero Save-File.")
    sleep(4)
    UserMenu()


def EXPGained():
    global clear
    system(clear)
    sleep(0.5)
    print(" EXP Gained Editor - Version 1.0")
    print(" This Function Edits The EXP Gained.")

    number = int(input(" EXP Gained: "))

    byte_array = bytearray(number.to_bytes(4, byteorder='big'))
    reversed_array = byte_array[::-1]

    with open('savegame', 'rb+') as bin_file:
        bin_file.seek(936)
        bin_file.write(reversed_array)
    
    print(f" Wrote Value of {number} to Generation Zero Save-File.")
    sleep(4)
    UserMenu()

Error_byte = b'\x0A'


if glob("savegame"):

    file0 = open('savegame', 'rb+')
    check_validity = file0.read(4)

    if check_validity != b'\x20\x46\x44\x41':
        system(clear)
        print(" Save-File in The Current Directory is Invalid.")
        print(" Error Code: Inv_Sav_Data_&&_0x01")
        sleep(3)

        with open('Save_File.log','a') as LogW:
            LogW.write("Save-Editor Provided With Invalid Data.")
            file1 = open('Save_File.log','rb+')
            file1.seek(38)
            file1.write(Error_byte)

            LogW.write("Bytes Scanned Below")
        
        with open('Save_File.log','rb+') as LogBin:
            LogBin.seek(58)
            LogBin.write(Error_byte)
            LogBin.write(check_validity)
            sleep(0.1)
        exit()





    with open('savegame','rb+') as save_file0:
        if path.exists("_backup"):
            num += 1
        else:
            mkdir('_backup') ; num += 1

        if num == 1:
            if path.exists("_backup\savegame"):
                remove('_backup\savegame')
                sleep(0.1)

            copy2('savegame', '_backup')
            
        print(" Generation Zero Save-File Has Been Backed-Up.")
        print(" Current Save-File is ready for Editing...")
        sleep(5)
        system(clear)

        def UserMenu():
            global num ; global clear
            system(clear)
            num = 1

            list0 = [1,2,3,0]
            system(clear)
            print(" Generation Zero Editor - Version 1.0")
            print(" ")
            print(" 1 = Edit Ammount of Skill Points.")
            print(" 2 = Edit Current Player Level.")
            print(" 3 = Ammount of EXP Gained. (Effects The Player Level).")
            print(" 0 = Exit The Current Editor.")
            print(" ")
            user_i = int(input(" Choose A Number: "))

            if user_i not in list0:
                UserMenu()

            if user_i == 0:
                system(clear)
                sleep(0.1)
                exit()

            if user_i == 1:
                SkillPoints()

            if user_i == 2:
                PlayerLevel()

            if user_i == 3:
                EXPGained()

        UserMenu()
        

    
else:
    print("No 'savegame' Save-File was Found.")