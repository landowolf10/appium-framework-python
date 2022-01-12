from framework.utils.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from framework.utils import constant_data, log_manager

class LoginScreen(BasePage):
    def __init__(self):
        super().__init__()

    title = (MobileBy.ACCESSIBILITY_ID, "Login")
    mailTextBox = (MobileBy.XPATH, "//android.view.View/android.widget.EditText[1]")
    passwordTextBox = (MobileBy.XPATH, "//android.view.View/android.widget.EditText[2]")
    loginButton = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Iniciar sesión']")
    registerButton = (MobileBy.XPATH, "//android.widget.Button[@content-desc='Crear cuenta']")

    def validateTitle(self, expectedTitle):
        currentTitle = self.getElementBy(*self.title).get_attribute('content-desc')
        print('Title: ' + currentTitle)
        
        if currentTitle == expectedTitle:
            log_manager.log_pass(f"Screen title is the expected '{expectedTitle}'")
        else:
            log_manager.log_fail(f"Title on screen is '{currentTitle}' but expecting '{expectedTitle}'")

    def validateLoginPage(self):
        currentTitle = self.getText(*self.title)

        if self.isVisible(*self.mailTextBox) and self.isVisible(*self.passwordTextBox) and self.isVisible(*self.loginButton) and self.isVisible(*self.registerButton):
            log_manager.log_pass("User is on login screen")
        else:
            log_manager.log_fail(f"User is not on login screen, current title is '{currentTitle}'")