import os , pyfiglet , time

os.system("clear")                                                                      os.system("clear")
os.system("clear")

class color :

          YELL = '\033[93m '                                                                      GREEN = '\033[92m '
          BLUE ='\033[94m '
          END = '\033[0m'

print ("   ")

result = pyfiglet.figlet_format('BYPASS CLOUD FLARE' , font = 'slant')

print (result)

print ("   ")
print (color.YELL + '''

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                              $
$   Code By : Mr Crazy8        $
$ Telegram : @lightgreen_heart $
$                              $
$                              $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

''' + color.END)
print ("  ")

print (color.BLUE + '''

[1] Test With mail

[2] Test With ftp

[3] Test With ssh

[4] Test With cpanel

[5] Test With whm

[99] Exit

''' + color.END)

print ("   ")

u = int(input(color.YELL + "Enter The Number ~# " + color.END))

print ("   ")
if u == 1:

    y = input(color.GREEN + "Enter The Url >>>" + color.END)

    print ("   ")

    os.system("ping "+"mail."+y)
if u == 2:

    q = input(color.GREEN + "Enter The Url >>>" + color.END)

    print ("   ")

    os.system("ping "+"ftp."+q)
if u == 3:

    w = input(color.GREEN + "Enter The Url >>>" + color.END)

    print ("   ")

    os.system("ping "+"ssh."+w)
if u == 4:

    i = input(color.GREEN + "Enter The Url >>>" + color.END)

    print ("   ")

    os.system("ping "+"cpanel."+i)
if u == 5:

    t = input(color.GREEN + "Enter The Url >>>" + color.END)

    print ("   ")

    os.system("ping "+"whm."+t)
if u == 99:

    os.system("clear")
