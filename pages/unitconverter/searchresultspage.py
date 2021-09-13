search_results_label_name = "Search results"
unit_name = "//android.widget.TextView[@text=\"%s\"]"


def clickonunit(self, unit):
    self.find_element_by_xpath(unit_name % unit).click()
