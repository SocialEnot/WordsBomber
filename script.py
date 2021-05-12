import keyboard
import time
import colorama
from colorama import Fore
colorama.init()
#by blotnoy
startweq = """|||WordsBomber|| - by blotnoy
|||version||| - v0.1 - python3
|||library||| - keyboard + time + colorama
|||text|||||| - 666000 - text
"""
print(startweq)
#by blotnoy
maintext = input('text: ')
print('launch via 5(sec)')
time.sleep(1)
print('launch via 4(sec)')
time.sleep(1)
print('launch via 3(sec)')
time.sleep(1)
print('launch via 2(sec)')
time.sleep(1)
print('launch via 1(sec)')
time.sleep(1)
print(Fore.YELLOW + '[?]' + Fore.WHITE + 'by BLOTNOY')
print('starting....')
def main():
	keyboard.write(maintext)
	print(Fore.GREEN + '[+]' + Fore.WHITE + 'отправленно')
for __ in range(666000):
	main()
	keyboard.send("enter")
	#by blotnoy


input()