Feature: package management using apt-get
 As a whonix user
 I need to be able to download and install packages
 To expand the the features of the system

 Scenario: update the package lists
  When: we programmatically run the command "sudo apt-get update" with "admin" privledges
  Then: the command executes successfully
  And: the list was updated

 Scenario: update whonix
  When: we programmatically run the command "sudo apt-get dist-upgrade" with "admin" privledges
  Then: the command executes successfully
  And: the system is up-to-date

 Scenario: install a package
  Given: the package vim is not currently installed
  When: we programmatically run the command "sudo apt-get install vim" with {admin} privledges
  Then: the command exectures successfully
  And: the package was installed

 Scenario: remove a package
 Given: the package vim is currently installed
 When: we programmatically run the command "sudo apt-get remove vim" with {admin} privledges
 Then: the command executes successfully
 And: the package was removed
 