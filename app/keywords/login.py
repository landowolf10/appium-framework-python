import sys, os
sys.path.append(os.path.join(os.getcwd(), '../..'))

from robot.api.deco import keyword
from app.pages.login_page import LoginScreen

login = LoginScreen()

@keyword(name="Validate title")
def validateTitle(expectedTitle):
    login.validateTitle(expectedTitle)

@keyword(name="User is on login page")
def validateLoginPage():
    login.validateLoginPage()