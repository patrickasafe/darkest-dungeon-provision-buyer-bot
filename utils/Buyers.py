import pyautogui
import time

from utils.click import click

from configs import SHOP_REGION


class BaseBuyer():
    # identifies pictures on screen when using the method 'identify'

    screenshot_path = ''
    dict: dict = None

    @classmethod
    def buy(cls, provisions_object):
        for key, provision in provisions_object.items():
            if provision > 0:

                # locate and buy items
                if pyautogui.locateOnScreen(
                        cls.dict[key], confidence=.60, region=SHOP_REGION, grayscale=.20):
                    provision_button = pyautogui.locateOnScreen(
                        cls.dict[key], confidence=.60, region=SHOP_REGION, grayscale=.20)  # set image to a variable
                    provision_button_x = provision_button[0]
                    provision_button_y = provision_button[1]
                    print(
                        f'{key} at ({provision_button_x}X, {provision_button_y}Y)')

                    for _ in range(provision):
                        click(provision_button_x, provision_button_y)
                        time.sleep(.3)
                    click(100, 100)
                    print(f"bought {str(provision)} {key}")
                # error
                else:
                    print(f'error, cannot find {key}')


class ProvisionBuyer(BaseBuyer):

    screenshot_path = 'utils/screenshots/provisions/'
    dict = {
        'food': f'{screenshot_path}food.png',
        'shovel': f'{screenshot_path}shovel.png',
        'torch': f'{screenshot_path}torch.png',
        'antivenom': f'{screenshot_path}antivenom.png',
        'key': f'{screenshot_path}key.png',
        'holy_water': f'{screenshot_path}holy_water.png',
        'medicinal_herbs': f'{screenshot_path}medicinal_herbs.png',
        'bandage': f'{screenshot_path}bandage.png',
    }
