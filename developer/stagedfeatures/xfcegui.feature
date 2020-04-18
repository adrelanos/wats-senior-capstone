Feature: Manipulate the XFCE environment using a keyboard
 As a inexperienced linux user
 I need to be able to use the computer without a terminal
 In order to properly utilize whonix's features.
 
 Background:
  Given the xfce gui testing hotkeys are configured

 Scenario: open mousepad with the application launcher
  Given "mousepad" is not running
  When I press the xfcegui hotkey "xfce-appfinder-collapsed"
  And I type "mousepad"
  And I press "enter"
  Then "mousepad" is running

 Scenario: create a new workspace, focus application, move that application to the new workspace, switch workspaces
  Given "mousepad" is running
  When a user presses the xfcegui hotkey "add workspace"
  And a user cycles applications until "mousepad" is active
  And a user moves the active apaplication to the new workspace
  The application is now in the proper workspace

 Scenario: close active application with hotkey
  Given "mousepad" is running
  And "mousepad" is the focused window
  When I press the key combination <alt><space>
  And I press c
  Then "mousepad is not running"

 