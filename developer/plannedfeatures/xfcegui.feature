Feature: Manipulate the XFCE desktop environment using a mouse and keyboard
 As a inexperienced linux user
 I need to be able to use the computer without a terminal
 In order to properly utilize whonix's features.
 
 Background:
  Given the user is logged in and the GUI is active
  And the window management hotkeys are properly set up

 Scenario: open mousepad with the application launcher
  When a user presses the "open application launcher" hotkey
  And a user types "mousepad"
  And a user presses "enter"
  Then "mousepad" opens successfully

 Scenario: create a new workspace, move an application to the new workspace, switch workspaces
  When a user presses the "add new workspace" hotkey
  And a user 
