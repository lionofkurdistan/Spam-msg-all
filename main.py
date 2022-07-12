import pyautogui
from time inport sleep

msg = input("Enter Youer Mag >> :")
num_msg = int(input("Cheose Youer Numbr Of Msg >> :"))
time_msg = float(input("Cheose Youer Time Of Msg >> : "))

for num in range(num_msg + 1):
	pyautogui.typewrite(msg)
	sleep(time_msg)
	pyautogui.press('enter')
	sleep(time_msg)
