from framework.utils.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from framework.utils import constant_data, log_manager

class CreateUser(BasePage):
    def __init__(self):
        super().__init__()

    title = (MobileBy.ACCESSIBILITY_ID, "Registro")
    nameTextBox = (MobileBy.XPATH, "//android.view.View/android.widget.EditText[1]")
    mailTextBox = (MobileBy.XPATH, "//android.view.View/android.widget.EditText[2]")
    passwordTextBox = (MobileBy.XPATH, "//android.view.View/android.widget.EditText[3]")
    createUserButton = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Crear cuenta']")
    registerButton = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Registrar cuenta']")
    returnToLoginButton = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Regresar al login']")
    errorTitle = (MobileBy.XPATH, "//android.view.View[@content-desc='Campos vacíos']")
    errorMessage = (MobileBy.XPATH, "//android.view.View[@content-desc='Favor de llenar todos los campos.']")
    popup_message = (MobileBy.XPATH, "//android.view.View[1]/android.view.View/android.view.View")
    popup_accept = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Aceptar']")

    def validateTitle(self, expectedTitle):
        currentTitle = self.getElementBy(*self.title).get_attribute('content-desc')
        
        if currentTitle == expectedTitle:
            log_manager.log_pass(f"Screen title is the expected '{expectedTitle}'")
        else:
            log_manager.log_fail(f"Title on screen is '{currentTitle}' but expecting '{expectedTitle}'")

    def validateRegisterScreen(self):
        currentTitle = self.getText(*self.title)
        isNameVisible = self.isVisible(*self.nameTextBox)
        isMailVisible = self.isVisible(*self.nameTextBox)
        isPasswordVisible = self.isVisible(*self.nameTextBox)

        if isNameVisible and isMailVisible and isPasswordVisible:
            log_manager.log_pass("User is on login screen")
        else:
            log_manager.log_fail(f"User is not on register screen, current title is '{currentTitle}'")

    def clickCreateUserButton(self):
        self.click_element(*self.createUserButton)

    def clickRegisterButton(self):
        self.click_element(*self.registerButton)

    def click_accept_popup_button(self):
        self.click_element(*self.popup_accept, button_name="Popup accept button")

    def verifyPopupTitle(self, expectedErrorTitle):
        currentErrorTitle = self.getElementBy(*self.errorTitle).get_attribute('content-desc')
        
        if currentErrorTitle == expectedErrorTitle:
            log_manager.log_pass(f"Error title is the expected '{expectedErrorTitle}'")
        else:
            log_manager.log_fail(f"Error title is '{currentErrorTitle}' but expecting '{expectedErrorTitle}'")

    def verifyPopupMessage(self, expectedErrorMessage):
        currentErrorMessage = self.getElementBy(*self.errorMessage).get_attribute('content-desc')
        
        if currentErrorMessage == expectedErrorMessage:
            log_manager.log_pass(f"Error message is the expected '{expectedErrorMessage}'")
        else:
            log_manager.log_fail(f"Error message is '{currentErrorMessage}' but expecting '{expectedErrorMessage}'")

    def verifyPopupVisibility(self, expectedVisibility):
        currentVisibility = self.isVisible(*self.popup_message)
        
        if currentVisibility == expectedVisibility:
            log_manager.log_pass(f"Popup visibility is the expected '{expectedVisibility}'")
        else:
            log_manager.log_fail(f"Popup visibility is '{currentVisibility}' but expecting '{expectedVisibility}'")