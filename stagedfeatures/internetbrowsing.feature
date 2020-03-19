Feature: internet browsing using the tor browser
 In order to use the whonix operating system
 As a whonix user
 I need to be able to browse the internet

 Scenario: open the tor browser, successfully connect to duckduckgo
  Given {whonixcheck} reports OK
  When I open the tor browser
  And I go to the webpage {https://duckduckgo.com}
  Then the page returns the code {200}

 Scenario: navigate to a whonix over clearnet and tor, download a file over tor
  Given {whonixcheck} reports OK
  When I open the tor browser
  And I go to the webpage {https://whonix.org}
  And I go to the webpage {http://dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion}
  And I download the file at {https://download.whonix.org/libvirt/15.0.0.8.7/Whonix-XFCE-15.0.0.8.7.libvirt.xz.asc}
  Then the file finishes downloading successfully
  and the file exists