import pyautogui
print(pyautogui.size())
import random
import time

xicon = 1413
yicon = 1365
xorb = 585
yorb = 283
xleft = 276
yleft = 320
xcenter = 350
ycenter = 350
xcenter2 = 380
ycenter2 = 270
xleft = 140
yleft = 300
xsafe = 280
ysafe = 422


def openapp():
	pyautogui.moveTo(1413, 1365, mousemove(), pyautogui.easeInQuad)
	time.sleep(quickerclick())
	pyautogui.click()

def quickclick():
	return round(random.uniform(0.7, 1.2), 2)

def quickerclick():
	return round(random.uniform(0.21, 0.62), 2)

def mousemove():
	return round(random.uniform(0.4, 2.0), 1)



def fix(coordinate):
	return coordinate+random.randint(-15, 15)


def orbtime():
	return random.randint(3, 5)

def reaggro1(x, y):
	openapp()
	pyautogui.moveTo(fix(x), fix(y), mousemove(), pyautogui.easeInQuad)
	time.sleep(quickerclick())
	pyautogui.click()

def between():
	time.sleep(random.randint(75, 180))

def quickbetween():
	time.sleep(round(random.uniform(10.7, 21.9), 2))

def orbdown():
	openapp()
	x = fix(xorb)
	y = fix(yorb)

	pyautogui.moveTo(x, y, mousemove(), pyautogui.easeInQuad)
	time.sleep(quickerclick())
	for i in range (0, orbtime()):
		pyautogui.click()
		time.sleep(quickerclick())

time.sleep(1)

while True:
	openapp()
	quickbetween()
	for i in range(0, random.randint(1, 5)):
		orbdown()
		quickbetween()
	test = random.randint(1, 4)
	if test == 1:
		reaggro1(xsafe, ysafe)
	if test == 2:
		reaggro1(xleft, yleft)
	if test == 3:
		reaggro1(xcenter, ycenter)
	if test == 4:
		reaggro1(xcenter2, ycenter2)
