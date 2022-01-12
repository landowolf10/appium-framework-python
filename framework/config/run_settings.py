"""
Date Created: 26/07/2021
@Author: Orlando Avila
Description: File to store run configuration variables for tests
"""

from framework.utils import constant_data

def loadConfig():
    settingsObj = {}

    settingsObj["platformName"] = constant_data.PLATFORM_NAME
    settingsObj["deviceName"] = constant_data.DEVICE_NAME
    settingsObj["appPackage"] = constant_data.APP_PACKAGE
    settingsObj["appActivity"] = constant_data.APP_ACTIVITY

    return settingsObj