import os , pyfiglet , time

os.system("clear")
os.system("clear")
os.system("clear")

class color :

          YELL = '\033[93m '
          GREEN = '\033[92m '
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

y = input(color.GREEN + "Enter The Url >>>" + color.END)

print ("   ")

os.system("ping "+"ftp."+y)
