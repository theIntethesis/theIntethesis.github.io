import pyautogui
from time import sleep

def test():
	for i in range(15):
		pyautogui.press(',')
		pyautogui.press('down')
		pyautogui.press('end')
	pyautogui.press('down')
	pyautogui.press(',')
	pyautogui.press('down')
	pyautogui.press('down')
	pyautogui.press('end')

def main():
	pyautogui.hotkey('alt', 'tab')
	sleep(0.1)
	for j in range(1, 360):
		pyautogui.press('delete')
		for i in range(18):
			pyautogui.press('down')

main()
# CDE x 15
# DCDDE