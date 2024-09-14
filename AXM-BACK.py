import os, sys, platform,time
 
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    os.system('chmod 777 FILEX')
    os.system('./FILEX')
    
elif bit == '32bit':
    os.system('xdg-open https://www.facebook.com/ARAFAT19847000');sleep(2)
    print("SORRY 32 BIT IS NOT UPLOADED")
 
