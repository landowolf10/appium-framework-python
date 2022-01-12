from framework.config.run_settings import loadConfig
from framework.utils import constant_data, config
from appium import webdriver

def getMobileDriver():
    #Verify if driver already exist on the config module, if so will return the current driver
    if config.isInstance == True:
        driver = config.driver
    else: #Creates a new driver
        driver = createDriver()

    #Set the driver on cfg module for later instances
    config.isInstance = True
    config.driver = driver

    return driver

def createDriver():
    #Load run settings from configuration file
    runSettings = loadConfig()
    platformName = runSettings["platformName"]
    deviceName = runSettings["deviceName"]
    appPackage = runSettings["appPackage"]
    appActivity = runSettings["appActivity"]

    desired_caps = {
        "platformName": platformName,
        "deviceName": deviceName,
        "appPackage": appPackage,
        "appActivity": appActivity
    }

    #Set driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver

def killDriver():
    currentDriver = None

    #Verify if driver already exist on the config module, if so will return the current driver
    if config.isInstance == True:
        currentDriver = config.driver
        currentDriver.quit()

    #Set the driver on config module for later instances
    config.isInstance = False
    config.driver = None