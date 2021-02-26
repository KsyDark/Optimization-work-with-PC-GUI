from win10toast import ToastNotifier
import time
from pyautogui import keyDown, keyUp
from os import startfile

keyDown ('alt')
keyDown ('F1')
keyUp ('F1')
keyUp ('alt')

print('ТОВАРИЩ!')
print('Разминай ноги!')

local_time = 1
local_time = local_time * 3600

def sport(event):
    """Запуск напоминания"""
    for timer in range(9):
        time.sleep(local_time)

        #Системное уведомление
        toast = ToastNotifier()
        toast.show_toast("СРОЧНО!ВАЖНО!","Размять ноги",duration=5, icon_path='sport.ico')

    timer

sport