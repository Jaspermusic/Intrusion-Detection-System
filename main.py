import cv2, os, time, datetime
import webbrowser

# video capture
cap = cv2.VideoCapture(0)
# set brigtness 100
cap.set(10,100)

# navigating root directory
user_name = os.getlogin()
directory = "C:/Users/{}".format(user_name)
os.chdir(directory)


try:
	os.mkdir('Bad People Images')
except:
	pass

os.chdir('Bad People Images')

if not os.path.exists('Passwords.txt'):
	with open('Passwords.txt', 'w') as f:
		f.write('Text in this file will be shown to others \n')
		f.write('Feel free to change them')
		f.close()

webbrowser.open('Passwords.txt')

# labelling folder with current time and date
real_time = datetime.datetime.now()
str_time = str(real_time)[:19].replace(':', '-')

try:
	os.mkdir(str_time)
except:
	pass

os.chdir(str_time)

for i in range(10):
	# capturing pics
	result, image = cap.read()

	# storing them
	cv2.imwrite("{}.png".format(i), image)

	# time to next pic
	time.sleep(2)

