import sys, os
sys.path.append(os.path.join(os.getcwd(), '../..'))

from robot.api.deco import keyword
from app.pages.create_user import CreateUser

cu = CreateUser()

@keyword(name="Validate title")
def validateTitle(expectedTitle):
    cu.validateTitle(expectedTitle)

@keyword(name="User is on register screen")
def validateRegisterScreen():
    cu.validateRegisterScreen()

@keyword(name="Click create user button")
def clickCreateUserButton():
    cu.clickCreateUserButton()

@keyword(name="Click register button")
def clickRegisterButton():
    cu.clickRegisterButton()

@keyword(name="Click accept popup button")
def click_accept_popup_button():
    cu.click_accept_popup_button()

@keyword(name="Verify popup title is")
def verifyPopupTitle(expectedErrorTitle):
    cu.verifyPopupTitle(expectedErrorTitle)

@keyword(name="Validate popup message is")
def verifyPopupMessage(expectedErrorMessage):
    cu.verifyPopupMessage(expectedErrorMessage)

@keyword(name="Verify popup visibility is")
def verifyPopupVisibility(expectedVisibility):
    cu.verifyPopupVisibility(expectedVisibility)