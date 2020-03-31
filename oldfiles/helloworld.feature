Feature: Demonstrate Hello World

     Scenario: run a basic test
          Given I have mousepad installed
	  When I open the application mousepad programmatically
	  And I type Hello world!
	  And I quit and save the file
	  Then the file will exist