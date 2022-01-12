import sys, os
sys.path.append(os.path.join(os.getcwd(), '../..'))

from robot.api.deco import keyword
from app.pages.calculator_screen import CalculatorScreen

cs = CalculatorScreen()

@keyword(name="Type number")
def clickNumber(number):
    cs.clickNumber(number)

@keyword(name="Validate typed number is")
def validateTyedNumber(expectedTypedNumber):
    cs.validateTyedNumber(expectedTypedNumber)

@keyword(name="Verify numbers on screen are")
def veifyNumbersOnScreen(expectedNumbers):
    cs.veifyNumbersOnScreen(expectedNumbers)

@keyword(name="Press delete button")
def clickDeleteButton():
    cs.clickDeleteButton()

@keyword(name="Verify screen is clean")
def validateClearedScreen():
    cs.validateClearedScreen()

@keyword(name="Type all numbers")
def clickAllNumbers():
    cs.clickAllNumbers()