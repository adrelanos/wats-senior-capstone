Feature: Testing basic terminal applications and functions.

     Scenario: test opening a terminal, writing to a text file
          Given we are testing nano and xterm
	  And the application(s) to be tested are installed
	  When we open a new xterm terminal
	  Then that file will have the text we wrote
