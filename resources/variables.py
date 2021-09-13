appiumserverurl = 'http://localhost:4723/wd/hub'
platformName = "Android"
platformVersion = "10"
deviceName = "generic_x86"
automationName = "UiAutomator2"
appPackage = "com.ba.universalconverter"
appActivity = ".MainConverterActivity"

capabilities = {
    "platformName": platformName,
    "platformVersion": platformVersion,
    "deviceName": deviceName,
    "automationName": automationName,
    "appPackage": appPackage,
    "appActivity": appActivity
}

unitconverterlabel = "Unit Converter"
unit1 = "Length"
unit2 = "Area"
unit3 = "Speed"
sourcemeasure1 = "Foot"
targetmeasure1 = "Centimeter"
sourcemeasure2 = "Acre"
targetmeasure2 = "Rood"
sourcemeasure3 = "Minutes per mile"
targetmeasure3 = "Mile per hour"
value1 = "5"
value2 = "11"
value3 = "32"
