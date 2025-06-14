import os
import pyautogui as py
import time
time.sleep(2)

def verify_waifus(waifus):
    found_waifu = py.locateCenterOnScreen(waifus)
    if found_waifu == None:
        return False
    else:
        return True

image_list = []
waifu_founded = False

# Get list of all files in current directory
directory = os.listdir('waifus')

# Find files that end with .png or .jpg and add to image_list
for file in directory:
    if file.endswith('.png') or file.endswith('.jpg'):
        image_list.append(file)

# Loop through list to find all the images

for image in image_list:
    waifu_in_screen = verify_waifus(f'waifus\{image}')
    print(waifu_in_screen)
    while waifu_in_screen == False:
        waifu_in_screen = verify_waifus(f'waifus\{image}')

        if waifu_in_screen == False:
            print('amogus')
            #for c in range(0, 10):
            #    time.sleep(4)
            #    py.write('$wa')
            #    time.sleep(0.5)
            #    py.press('Enter')
            #time.sleep(3600)
        else:
            break

time.sleep(2)
py.click(py.locateCenterOnScreen('marrybutton.png'))
