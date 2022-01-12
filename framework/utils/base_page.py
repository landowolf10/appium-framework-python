"""
Date Created: 27/07/2021
@Author: Orlando Avila
Description: Base page class
"""

from framework.config import clients
from framework.utils import timeouts, constant_data, log_manager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
import time
from robot.api import logger

class BasePage():
    def __init__(self):
        self.driver = clients.getMobileDriver()

    # ------- Driver functions --------
    def getDriver(self):
        return self.driver

    def closeAllScreens(self):
        clients.killDriver()

    def launchApp(self):
        return self.driver.launch_app()

    # ------- Element functions --------
    def getElementBy(self,id_type, id_text):
        element = self.waitUntilVisible(id_type, id_text)

        return element

    def getElementsBy(self, id_type, id_text):
        elements = self.waitForElements(id_type, id_text)
        return elements

    # ------- Action functions --------
    def click_element(self, id_type, id_text, button_name = "Unknown", wait_after_click = timeouts.WAIT_AFTER_CLICK):
        self.waitUntilVisible(id_type, id_text)
        element = self.getElementBy(id_type, id_text)
        log_manager.log_info(f"Clicking {button_name} button...")
        element.click()
        time.sleep(wait_after_click)

    def click(self, element, button_name="Unknown", wait_after_click = timeouts.WAIT_AFTER_CLICK):
        log_manager.log_info(f"Clicking {button_name} button...")
        element.click()
        time.sleep(wait_after_click)
        
    def type_text(self, id_type, id_text, text):
        element = self.waitForElement(id_type, id_text)
        element.clear()
        log_manager.log_info(f"Typing {text} on text field...")
        element.send_keys(text)
        time.sleep(timeouts.WAIT_AFTER_TYPE)

    # ------- Info/Properties functions --------
    def getText(self, id_type, id_text):
        element = self.waitUntilVisible(id_type, id_text)
        return element.text

    def getAttribute(self, id_type, id_text, attribute_name):
        element = self.getElementBy(id_type, id_text)
        return element.get_attribute(attribute_name)

    def isSelected(self, id_type, id_text):
        self.waitUntilVisible(id_type, id_text)
        element = self.getElementBy(id_type, id_text)
        element.is_selected()

    def isEnabled(self, id_type, id_text):
        self.waitUntilVisible(id_type, id_text)
        element = self.getElementBy(id_type, id_text)
        element.is_enabled()

    def isVisible(self, id_type, id_text):
        element = self.waitUntilVisible(id_type, id_text)
        if element != None:
            return True

        return False

    def isExist(self,id_type, id_text):
        try:
            element = self.waitUntilVisible(id_type, id_text)
            if element != None:
                return True
            return False
        except:
            return False

     # ------- Wait functions -----------
    def waitUntil(self, condition, max_wait_sec = timeouts.WAIT_FOR_CONTROL):
        self.driver.implicitly_wait(0)
        wait = WebDriverWait(self.driver, max_wait_sec)
        return wait.until(condition)

    # Returns the element if visible, returns None if not
    def waitUntilVisible(self, id_type, id_text,max_wait_sec=timeouts.WAIT_FOR_CONTROL):
        try:
            return self.waitUntil(
            expected_conditions.presence_of_element_located((id_type, id_text)),max_wait_sec)
        except:
           log_manager.log_info(f"Element not visible after {max_wait_sec} seconds...")

    def waitUntilNotVisible(self, id_type, id_text,max_wait_sec=timeouts.WAIT_FOR_CONTROL):
        return self.waitUntil(
            expected_conditions.invisibility_of_element_located((id_type, id_text)),max_wait_sec)

    def waitUntilClickable(self, id_type, id_text,max_wait_sec=timeouts.WAIT_FOR_CONTROL):
        return self.waitUntil(
            expected_conditions.element_to_be_clickable((id_type, id_text)),max_wait_sec)

    def waitForElement(self, id_type, id_text,max_wait_sec=timeouts.WAIT_FOR_CONTROL):
        return self.waitUntil(
            expected_conditions.presence_of_element_located((id_type, id_text)),max_wait_sec)

    def waitForElements(self, id_type, id_text,max_wait_sec=timeouts.WAIT_FOR_CONTROL):
        return self.waitUntil(
            expected_conditions.presence_of_all_elements_located((id_type, id_text)),max_wait_sec)