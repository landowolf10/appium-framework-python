from framework.utils.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from framework.utils import constant_data, log_manager

class CalculatorScreen(BasePage):
    def __init__(self):
        super().__init__()

    formula = (MobileBy.ID, "com.google.android.calculator:id/formula")
    result = (MobileBy.ID, "com.google.android.calculator:id/result_preview")
    divide_button = (MobileBy.ID, "com.google.android.calculator:id/op_div")
    multiply_button = (MobileBy.ID, "com.google.android.calculator:id/op_mul")
    substract_button = (MobileBy.ID, "com.google.android.calculator:id/op_sub")
    add_button = (MobileBy.ID, "com.google.android.calculator:id/op_add")
    equals_button = (MobileBy.ID, "com.google.android.calculator:id/eq")
    delete_button = (MobileBy.ID, "com.google.android.calculator:id/del")

    def clickNumber(self, number):
        stringNumber = str(number)
        selectedNumber = (MobileBy.ID, "com.google.android.calculator:id/digit_" + stringNumber)

        self.click_element(*selectedNumber, button_name="Number " + stringNumber, wait_after_click=3)
        
    def validateTyedNumber(self, expectedTypedNumber):
        currentNumber = self.getText(*self.formula)

        if currentNumber == expectedTypedNumber:
            log_manager.log_pass(f"Number on screen is the expected '{expectedTypedNumber}'")
        else:
            log_manager.log_fail(f"Number on screen is '{currentNumber}' but expecting '{expectedTypedNumber}'")

    def validateClearedScreen(self):
        currentElement = self.getText(*self.formula)

        if currentElement == "":
            log_manager.log_pass(f"The screen has been cleared successfully")
        else:
            log_manager.log_fail(f"Number on screen is '{currentElement}' but expecting to be cleared")

    def veifyNumbersOnScreen(self, expectedNumbers):
        currentNumbers = self.getText(*self.formula)

        if currentNumbers == expectedNumbers:
            log_manager.log_pass(f"Numbers on screen are the expected '{expectedNumbers}'")
        else:
            log_manager.log_fail(f"Number on screen are '{currentNumbers}' but expecting '{expectedNumbers}'")

    def clickAllNumbers(self):
        for number in range(10):
            self.clickNumber(number)

        formulaTxt = self.getText(*self.formula)

    def clickDeleteButton(self):
        self.click_element(*self.delete_button, button_name="Delete", wait_after_click=3)