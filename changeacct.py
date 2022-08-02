import os
import sys

check = input('Need to force close the game before start. Proceed? (Y/N)\n')
if check == 'Y' or check == 'y':
    
    os.system("TASKKILL /F /IM MASS.exe")
    acct = input('Which account were you in?: ')
    items = os.listdir(r'E:\ROK')
    
    fileList = [name for name in items if name.startswith("save -")]
    
    print('Saved accounts: ') 
    for cnt, fileName in enumerate(fileList, 0):
        sys.stdout.write("[%d] %s\n\r" % (cnt, fileName))
     
    choice = int(input("Choose account -> [0-%s]: " % cnt))
    destacct = fileList[choice].split(' - ')
    print('Changing from '+ acct + ' to ' + destacct[1] + "...")
    print('Saving previous account as save - '+acct+'...')
    
    os.chdir(r'E:\ROK')
    os.rename('save', 'save - ' + acct)
    os.rename(fileList[choice], 'save')
    
    print('Done!')
    os.startfile("E:\ROK\launcher.exe")
else:
    print('OK run me again when u ready ;)')






    

