Feature: Conversions in unit converter

    Scenario: Open the unit converter app
        Given I open the unit converter app
        Then The app will open

    Scenario: Go unit converter sidebar
        Given Application is open
        When I click on the menu button
        Then I should see the unit converter menu

    Scenario: Select Length
        Given I'm in the unit converter menu
        When I click on Length
        Then It should display the Length converter

    Scenario: Select measurements
        Given I'm in Length converter
        When I select the source measure to be Foot
        And I select the target measure to be Centimeter
        Then The source measure is Foot
        And The target measure is Centimeter

    Scenario: Convert from Foot to Centimeter
        Given Source measure is Foot and target measure is Centimeter
        When I input 5
        Then Value is converted to Centimeter which equals to 30.48 per foot

    Scenario: Go unit converter sidebar
        Given Application is open
        When I click on the menu button
        Then I should see the unit converter menu

    Scenario: Select Area
        Given I'm in the unit converter menu
        When I click on Area
        Then It should display the Area converter

    Scenario: Select measurements
        Given I'm in Area converter
        When I select the source measure to be Acre
        And I select the target measure to be Rood
        Then The source measure is Acre
        And The target measure is Rood

    Scenario: Convert from Acre to Rood
        Given Source measure is Acre and target measure is Rood
        When I input 11
        Then Value is converted to Rood which equals to 4 per Acre

    Scenario: Search for Speed unit
        Given Application is open
        When I search for Speed
        Then It should display the Speed converter

    Scenario: Select measurements
        Given I'm in Speed converter
        When I select the source measure to be Minutes per mile
        And I select the target measure to be Mile per hour
        Then The source measure is Minutes per mile
        And The target measure is Mile per hour

    Scenario: Convert from Minutes per mile to Kilometer per hour
        Given Source measure is Minutes per mile and target measure is Mile per hour
        When I input 32
        Then Value is converted to Mile per hour which equals to 60 divided by Minutes per mile