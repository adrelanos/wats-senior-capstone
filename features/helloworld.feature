Feature: Demonstrate Hello World

     Scenario: run a basic test
          Given we have nano installed
	  When we open mousepad
	  And we write hello world
	  And we quit and save the file
	  Then the file will exist
	  