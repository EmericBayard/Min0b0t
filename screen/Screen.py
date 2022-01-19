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
    def print(self) -> None:
        print('Width:', self.width)
        print('Height:', self.height)
    
    """Refresh resolution and screen"""
    def refresh(self) -> None:
        self.s = pya.screenshot()
        self.width, self.height = pya.size()
    
    """Return true if the screen is Dofus window"""
    """ WIP """
    def isDofus(self) -> bool:
        img = Image.open(glo.top_right_button) 
        return not isinstance(pya.locate(img, self.s, grayscale=False), type(None))
    

