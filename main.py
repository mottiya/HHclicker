import keyboard as kb
import pyautogui as pgui
from pyscreeze import Box
import telegram_bot
import os

name_computer = input("Введите имя компьютера: ")
telegram_bot.name_computer = name_computer

print(name_computer, ': ', 'start process...')
telegram_bot.send_massage('start process...')


counts = 0
while kb.is_pressed("Esc") == False:
    counts += 1
    try:
        if counts == 10:
            telegram_bot.send_massage('no stars or buttons next on the screen')
            print(name_computer, ': ', 'no stars or buttons next on the screen')
            break
        button = pgui.locateOnScreen("Letters\\Star.PNG", confidence=0.9)

        if button:
            counts = 0
            print(name_computer, ' button: ', button)
            pgui.click(button)

            name = button._asdict()

            name["left"] = name["left"] + 20

            pgui.sleep(1)
            pgui.moveTo(120, 180, duration=1)
            pgui.sleep(1)

            save_button = pgui.locateOnScreen("Letters\\Save.PNG", confidence=0.9)
            if not save_button:
                continue
            clickbox = Box(save_button.left, save_button.top - 150, save_button.width, save_button.height)

            pgui.moveTo(clickbox.left + clickbox.width / 2, clickbox.top, duration=1)
            pgui.click(clickbox)

            pgui.sleep(1)
            save_button = pgui.locateOnScreen("Letters\\Save.PNG", confidence=0.9)

            pgui.moveTo(save_button.left + save_button.width / 2, save_button.top, duration=1)
            pgui.click(save_button)

            pgui.sleep(1)
            pgui.moveTo(name["left"], name["top"])
            pgui.click(Box(**name))
            pgui.sleep(3)

            limit = pgui.locateOnScreen("Letters\\Limit500.PNG", confidence=0.9)
            if limit != None:
                telegram_bot.send_massage('500 limit overflowed')
                print(name_computer, ': ', '500 limit overflowed')
                break

            for i in range(10):
                pgui.sleep(0.2)
                pgui.scroll(-150)

            cross = pgui.locateOnScreen("Letters\\Cross.PNG", confidence=0.9)

            pgui.moveTo(cross.left, cross.top, duration=1)
            pgui.click(cross)

            pgui.moveTo(120, 120)

            pgui.scroll(-350)
            pgui.moveTo(132, 250)
            pgui.sleep(1)

        next_button = pgui.locateOnScreen("Letters\\NextPage.PNG")
        next_button2 = pgui.locateOnScreen("Letters\\Next.PNG")

        if next_button:
            pgui.click(next_button)
            pgui.sleep(5)

        elif next_button2:
            pgui.click(next_button2)
            pgui.sleep(5)
        else:
            pgui.scroll(-250)
            pgui.sleep(2)
    except:
        telegram_bot.send_massage('throw some exception')
        print(name_computer, ': ', 'throw some exception')
        break
os.system("pause")
