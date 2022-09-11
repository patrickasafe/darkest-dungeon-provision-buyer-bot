import time
import pyautogui

from utils.Buyers import ProvisionBuyer
from utils.Identifiers import DungeonIdentifier, DungeonLengthIdentifier

from utils.sum_provisions import sum_provisions
from utils.provisions_data import provisions

from configs import TIME_WITHOUT_LOOP


# Here is the master function:
def buy_provisions():
    # if provision screen appears, do as below:
    if pyautogui.locateOnScreen('utils/screenshots/provisions/provision_screen.png'):
        print('Provisions seller identified...')

        # identify dungeon and length
        selected_dungeon: str = DungeonIdentifier.identify()
        print(f'Dungeon identified: {selected_dungeon}')
        selected_dungeon_length: str = DungeonLengthIdentifier.identify()
        print(f'Dungeon length identified: {selected_dungeon_length}')

        # sum provisions used in expedition
        provisions_summed: dict = sum_provisions(
            provisions['default'][selected_dungeon_length],
            provisions[f"{selected_dungeon}_modifiers"][selected_dungeon_length])
        print('Necessary provisions identified...')

        # buy provisions
        ProvisionBuyer.buy(provisions_summed)

        print('Provisions bought...')

        time.sleep(TIME_WITHOUT_LOOP)
