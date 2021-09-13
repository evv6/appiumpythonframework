from appium import webdriver
from behave import *
from pages.unitconverter import mainpage, menupage, searchresultspage, selectorpage
from pages.unitconverter.searchresultspage import *
from resources.variables import *


@given(u'I open the unit converter app')
def step_impl(context):
    global driver
    driver = webdriver.Remote(appiumserverurl, capabilities)
    driver.implicitly_wait(30)


@then(u'The app will open')
def step_impl(context):
    mainpage.validatecurrentpackage(driver)


@given(u'Application is open')
def step_impl(context):
    mainpage.validatecurrentpackage(driver)


@when(u'I click on the menu button')
def step_impl(context):
    mainpage.clickonmenubutton(driver)


@then(u'I should see the unit converter menu')
def step_impl(context):
    mainpage.validatelabelname(driver, unitconverterlabel)


@given(u'I\'m in the unit converter menu')
def step_impl(context):
    mainpage.validatelabelname(driver, unitconverterlabel)


@when(u'I click on Length')
def step_impl(context):
    menupage.selectunit(driver, unit1)


@when(u'I click on Area')
def step_impl(context):
    menupage.selectunit(driver, unit2)


@when(u'I search for Speed')
def step_impl(context):
    mainpage.searchunit(driver, unit3)
    mainpage.validatelabelname(driver, search_results_label_name)
    searchresultspage.clickonunit(driver, unit3)


@then(u'It should display the Length converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit1)


@then(u'It should display the Area converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit2)


@then(u'It should display the Speed converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit3)


@given(u'I\'m in Length converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit1)


@given(u'I\'m in Area converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit2)


@given(u'I\'m in Speed converter')
def step_impl(context):
    mainpage.validatelabelname(driver, unit3)


@when(u'I select the source measure to be Foot')
def step_impl(context):
    mainpage.clickonsourceselector(driver)
    selectorpage.selectunit(driver, sourcemeasure1)


@when(u'I select the target measure to be Centimeter')
def step_impl(context):
    mainpage.clickontargetselector(driver)
    selectorpage.selectunit(driver, targetmeasure1)


@when(u'I select the source measure to be Acre')
def step_impl(context):
    mainpage.clickonsourceselector(driver)
    selectorpage.selectunit(driver, sourcemeasure2)


@when(u'I select the target measure to be Rood')
def step_impl(context):
    mainpage.clickontargetselector(driver)
    selectorpage.selectunit(driver, targetmeasure2)


@when(u'I select the source measure to be Minutes per mile')
def step_impl(context):
    mainpage.clickonsourceselector(driver)
    selectorpage.selectunit(driver, sourcemeasure3)


@when(u'I select the target measure to be Mile per hour')
def step_impl(context):
    mainpage.clickontargetselector(driver)
    selectorpage.selectunit(driver, targetmeasure3)


@then(u'The source measure is Foot')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure1)


@then(u'The target measure is Centimeter')
def step_impl(context):
    mainpage.verifytargetmeasure(driver, targetmeasure1)


@then(u'The source measure is Acre')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure2)


@then(u'The target measure is Rood')
def step_impl(context):
    mainpage.verifytargetmeasure(driver, targetmeasure2)


@then(u'The source measure is Minutes per mile')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure3)


@then(u'The target measure is Mile per hour')
def step_impl(context):
    mainpage.verifytargetmeasure(driver, targetmeasure3)


@given(u'Source measure is Foot and target measure is Centimeter')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure1)
    mainpage.verifytargetmeasure(driver, targetmeasure1)


@given(u'Source measure is Acre and target measure is Rood')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure2)
    mainpage.verifytargetmeasure(driver, targetmeasure2)


@given(u'Source measure is Minutes per mile and target measure is Mile per hour')
def step_impl(context):
    mainpage.verifysourcemeasure(driver, sourcemeasure3)
    mainpage.verifytargetmeasure(driver, targetmeasure3)


@when(u'I input 5')
def step_impl(context):
    mainpage.clickonclearbutton(driver)
    mainpage.inputnumber(driver, value1)


@when(u'I input 11')
def step_impl(context):
    mainpage.clickonclearbutton(driver)
    mainpage.inputnumber(driver, value2)


@when(u'I input 32')
def step_impl(context):
    mainpage.inputnumber(driver, value3)


@then(u'Value is converted to Centimeter which equals to 30.48 per foot')
def step_impl(context):
    mainpage.verifytargetvalue(driver, str(int(value1)*30.48))


@then(u'Value is converted to Rood which equals to 4 per Acre')
def step_impl(context):
    mainpage.verifytargetvalue(driver, str(int(value2)*4))


@then(u'Value is converted to Mile per hour which equals to 60 divided by Minutes per mile')
def step_impl(context):
    mainpage.verifytargetvalue(driver, str(60/int(value3)))
