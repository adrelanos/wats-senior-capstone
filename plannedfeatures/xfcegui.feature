Feature: Manipulate the XFCE desktop environment using a mouse and keyboard
 As a inexperienced linux user
 I need to be able to use the computer without a terminal
 In order to properly utilize whonix's features.

 Scenario: open an application with the application launcher
  Given the user is logged in and the GUI is active
  When a user clicks on the "application launcher"
  And selects the "utilities" tab in the application launcher
  And selects "mousepad" from the tab
  Then "mousepad" opens successfully
  
 Scenario: close an open applcation with the mouse
  Given "mousepad" is open
  When a user focuses on "mousepad"
  And clicks the close button
  And clicks confirm
  Then "mousepad" is closed"

 Scenario: search for an application and open it
  Given the user is logged in and the GUI is active
  When a user clicks on the "application launcher"
  And clicks on the "search field"
  And types in "mousepad"
  And presses "enter"
  Then mousepad opens successfully
