import sys, os
sys.path.append(os.path.join(os.getcwd(), '../..'))

from robot.api.deco import keyword
from framework.utils.base_page import BasePage

bp = BasePage()

@keyword(name="Close all screens")
def closeAllScreens():
    bp.closeAllScreens()

@keyword(name="Launch application")
def launchApp():
    bp.launchApp()