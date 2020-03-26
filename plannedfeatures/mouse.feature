Feature: use the mouse to manipulate the desktop gui
 As an inexperience whonix user
 I need to be able to use the mouse to manipulate the desktop
 In order to have a more accessible experience
 
Scenario: minimize and maximize an application by clicking on it's icon

Scenario: open a text file on the desktop

Scenario: do other mouse stuff that mouse only - verify the mouse works

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
