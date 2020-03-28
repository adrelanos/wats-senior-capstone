Feature: package management using apt-get
 As a whonix user
 I need to be able to update, download, and install packages
 To expand the the features of the system

 Scenario: update the package lists
  When we run the terminal command sudo apt-get --assume-yes update with admin privledges
  Then the command(s) executed successfully

 Scenario: update whonix
  When we programmatically run the command sudo apt-get --assume-yes dist-upgrade with admin privledges
  Then the command(s) executed successfully

 Scenario: install a package
  Given the package debug-misc is not installed
  When we programmatically run the command sudo apt-get --assume-yes install vim  with admin privledges
  Then the command(s) executed successfully
  And the application is installed

 Scenario: remove a package
  Given the package debug-misc is currently installed
  When we programmatically run the command sudo apt-get --assume-yes remove vim with admin privledges
  Then the command(s) executed successfully
  And the application is not installed