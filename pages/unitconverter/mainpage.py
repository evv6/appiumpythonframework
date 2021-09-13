from appium.webdriver.common.touch_action import TouchAction
from resources.variables import *
import time

menu_button_id = "Open navigation drawer"
search_button_id = "Search"
label_name = "//android.widget.TextView[@text=\"%s\"]"
source_measure = "(//android.widget.RelativeLayout/android.widget.TextView)[1]"
target_measure = "(//android.widget.RelativeLayout/android.widget.TextView)[2]"
source_selector = "(//android.widget.ImageView[@content-desc=\"Drop down\"])[1]"
target_selector = "(//android.widget.ImageView[@content-desc=\"Drop down\"])[2]"
numpad_button = "//android.widget.Button[@text=\"%s\"]"
clear_button = "C"
target_value = "com.ba.universalconverter:id/target_value"

serachbar = "com.ba.universalconverter:id/search_src_text"


def getcurrentpackage(self):
    package = self.current_package
    return package


def validatecurrentpackage(self):
    assert getcurrentpackage(self) == appPackage


def validatelabelname(self, labelname):
    assert True == self.find_element_by_xpath(
        label_name % labelname).is_displayed()


def clickonmenubutton(self):
    self.find_element_by_accessibility_id(menu_button_id).click()


def clickonsearchbutton(self):
    self.find_element_by_accessibility_id(search_button_id).click()


def inputunit(self, unit):
    self.find_element_by_id(serachbar).send_keys(unit)


def getsourcemeasure(self):
    measure = self.find_element_by_xpath(source_measure).text
    return measure


def gettargetmeasure(self):
    measure = self.find_element_by_xpath(target_measure).text
    return measure


def verifysourcemeasure(self, unit):
    assert unit == getsourcemeasure(self)


def verifytargetmeasure(self, unit):
    assert unit == gettargetmeasure(self)


def clickonsourceselector(self):
    self.find_element_by_xpath(source_selector).click()


def clickontargetselector(self):
    self.find_element_by_xpath(target_selector).click()


def clickonnumber(self, number):
    self.find_element_by_xpath(numpad_button % number).click()


def clickonclearbutton(self):
    self.find_element_by_xpath(numpad_button % clear_button).click()


def searchunit(self, unit):
    clickonsearchbutton(self)
    inputunit(self, unit)
    time.sleep(2.5)
    TouchAction(self).tap(x=984, y=1690).perform()


def inputnumber(self, number):
    for digit in number:
        clickonnumber(self, digit)


def gettargetvalue(self):
    number = self.find_element_by_id(target_value).text
    return number


def verifytargetvalue(self, target):
    assert gettargetvalue(self) == target
