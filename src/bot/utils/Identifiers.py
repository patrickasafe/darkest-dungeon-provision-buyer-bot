import pyautogui

from utils.screen_resolution_adjuster import relative_aspect_resolution_converter

from configs import GAME_SCREEN_RESOLUTION, ORIGINAL_DUNGEON_AND_LENGTH_REGION

LENGTH_REGION = relative_aspect_resolution_converter(
    ORIGINAL_DUNGEON_AND_LENGTH_REGION, GAME_SCREEN_RESOLUTION)


class BaseIdentifier():
    # identifies pictures on screen when using the method 'identify'

    screenshot_path = ''
    dict: dict = None

    @classmethod
    def identify(cls) -> str:
        for key, value in cls.dict.items():
            if pyautogui.locateOnScreen(value, region=LENGTH_REGION, confidence=.9):
                identified = pyautogui.locateOnScreen(
                    value, region=LENGTH_REGION, confidence=.9)
                print(
                    f'identified {key} at ({identified[0]}X, {identified[1]}Y)')
                return key


class DungeonIdentifier(BaseIdentifier):

    screenshot_path = 'utils/screenshots/dungeon_name/'

    dict = {
        'cove': f'{screenshot_path}cove.png',
        'darkest_dungeon': f'{screenshot_path}darkest_dungeon.png',
        'farmstead': f'{screenshot_path}farmstead.png',
        'ruins': f'{screenshot_path}ruins.png',
        'warrens': f'{screenshot_path}warrens.png',
        'weald': f'{screenshot_path}weald.png'
    }


class DungeonLengthIdentifier (BaseIdentifier):

    screenshot_path = 'utils/screenshots/dungeon_length/'

    dict = {
        'short': f'{screenshot_path}short.png',
        'medium': f'{screenshot_path}medium.png',
        'long': f'{screenshot_path}long.png',
    }
