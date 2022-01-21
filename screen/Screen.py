import pyautogui as pya
from PIL import Image
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import globalVariable.globalVariable as glo


class Screen:
    """Class that determine the screen caracteristic of the player."""
    width = 0
    height = 0
    s = None
    resolution = (width,height)

    """Constructor"""
    def __init__(self) -> None:
        self.width, self.height = pya.size()
        s = pya.screenshot()

    """Print width and height of screen"""
    @classmethod
    def print(self) -> None:
        print('Width:', self.width)
        print('Height:', self.height)
    
    """Refresh resolution and screen"""
    @classmethod
    def refresh(self) -> None:
        self.s = pya.screenshot()
        self.width, self.height = pya.size()
    
    """Return true if the screen is Dofus window"""
    @classmethod
    def isDofus(self) -> bool:
        img = Image.open(glo.top_right_button) 
        return not isinstance(pya.locate(img, self.s, grayscale=False), type(None))

    """Return position of @par"""
    @classmethod
    def getCoordinate(self, path: str) -> tuple:
        img = Image.open(path) 
        return pya.center(pya.locate(img, self.s, grayscale=False, confidence=0.9))
    
    """Click at coordinate and Return void """
    @staticmethod
    def clickAtCoordinate( x: int, y: int) -> None:
        pya.click(x/2, y/2)
    """Click to close a window and Return void """
    @staticmethod
    def closeAWindow(self, path: str) -> None:
        x, y = self.getCoordinate(glo.button_close_window)
        Screen.clickAtCoordinate(x, y)


    
    

    



    

