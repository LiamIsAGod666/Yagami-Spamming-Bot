import random
import time
from io import BytesIO
import win32clipboard
from PIL import Image
from pynput.keyboard import Key, Controller
keyboard = Controller()

picture_list = ['light_pictures\light1.jpg','light_pictures\light2.jpg','light_pictures\light3.jpg',
                'light_pictures\light4.jpg','light_pictures\light5.jpg','light_pictures\light6.jpg',
                'light_pictures\light7.jpg','light_pictures\light8.jpg','light_pictures\light9.jpg',
                'light_pictures\light10.jpg','light_pictures\light11.jpg','light_pictures\light12.jpg',
                'light_pictures\light13.jpg','light_pictures\light14.jpg','light_pictures\light15.jpg',
                'light_pictures\light16.jpg','light_pictures\light17.jpg','light_pictures\light18.jpg',
                'light_pictures\light19.jpg','light_pictures\light20.jpg',]
message_list = ["OMG HE'S SO HOT","He's so kawaiiiiiii!","I wanna marry him","I want to be his bride", "YagamI, I love YOUUUUOUOUOUO",
 "I am going to marry Light Yagami", "YAGAAAMII, MARRY MEEEEEEE!!!","those brown and majestic eyes, MARRY MEEE", "Light is soooooo cuuuute","kiss meee"]
def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
input('press enter ')
x = 10
for i in range(10):
    print(x)
    x-=1
    time.sleep(1)
while True:
    random_message = random.choice(message_list)
    random_picture = random.choice(picture_list)
    image = Image.open(random_picture)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    time.sleep(0.45)
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    keyboard.type(random_message)
    time.sleep(0.40)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
