selected_unit = "new UiScrollable(new UiSelector().scrollable(true))" + \
    ".scrollIntoView(new UiSelector().text(\"%s\"))"


def selectunit(self, unit):
    self.find_element_by_android_uiautomator(selected_unit % unit).click()
