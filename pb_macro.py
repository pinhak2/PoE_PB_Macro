# Bloco de importação corrigido
import pyautogui
from pyautogui import ImageNotFoundException
import time
import keyboard

# O resto do seu código continua abaixo...
# You have to change
pb_buff_image_url = "images\PB_BUFF.PNG"
# ...etc
pb_full_image_url = "images\PB_FULL.PNG"
pb_default_image_url = "images\PB_DEFAULT.PNG"

left_of_skill_button = 1630
top_of_skill_button = 1015
width_of_skill_button = 200
height_of_skill_button = 300

left_of_buff_area = 0
top_of_buff_area = 0
width_of_buff_area = 1400
height_of_buff_area = 70

# May need to change
pb_keyboard_key = "t"

# Do not change unless you know how to program
frequency_of_search_in_seconds = 0.25
skillInCooldown = False

skillUptime = 8.3
skillCooldown = 0.1
skillDelay = skillUptime + skillCooldown


def searchImage(imageLink, left, top, width, height):
    try:
        return pyautogui.locateOnScreen(
            imageLink, region=(left, top, width, height), grayscale=True, confidence=0.8
        )
    except ImageNotFoundException:
        # Se o pyautogui falhar (nao encontrar), retorna None em vez de quebrar
        return None


def cooldown():
    global skillInCooldown
    skillInCooldown = True
    time.sleep(skillDelay)
    skillInCooldown = False


def pressPlagueBearerKeyboardKey(activateCooldown=True):
    keyboard.send(pb_keyboard_key)
    if activateCooldown:
        cooldown()


def usePlageBearer():
    if (
        searchImage(
            pb_full_image_url,
            left_of_skill_button,
            top_of_skill_button,
            width_of_skill_button,
            height_of_skill_button,
        )
        == None
    ):
        print("Plague Bearer not ready!")
        time.sleep(frequency_of_search_in_seconds)
        return
    print("Using Plague Bearer...")
    pressPlagueBearerKeyboardKey()


def activatePlagueBearer():
    time.sleep(skillCooldown)
    if (
        searchImage(
            pb_buff_image_url,
            left_of_buff_area,
            top_of_buff_area,
            width_of_buff_area,
            height_of_buff_area,
        )
        == None
    ):
        print("Activating Plague Bearer ....")
        pressPlagueBearerKeyboardKey(False)


def skillInPlace():
    if (
        searchImage(
            pb_default_image_url,
            left_of_skill_button,
            top_of_skill_button,
            width_of_skill_button,
            height_of_skill_button,
        )
        == None
    ):
        print("Plague Bearer not in place!")
        return False
    print("Plague Bearer Bearer is set!")
    return True


while True:
    if skillInPlace():
        while not skillInCooldown:
            usePlageBearer()
            activatePlagueBearer()
