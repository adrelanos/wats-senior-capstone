Feature: communicate over various chat clients
 As a whonix user
 I need to be able to communicate using many applications
 So that I can use whonix effectively

 Scenario: communicate using matrix
  Given: {matrix} is installed
  When: a user opens {matrix}
  And: connects to the whonix chat
  Then: they successfully connect

 Scenario: communicate using hexchat irc
  Given: {hexchat} is installed
  When: a user opens {hexchat}
  And: connects to the whonix hexchat server
  Then: they successfully connect to the whonix support irc

 Scenario: communicate using telegram
  Given: {telegram} is installed
  When: a user opens {telegram}
  And: connects to the whonix telegram server
  Then: they successfully connect to the whonix server

