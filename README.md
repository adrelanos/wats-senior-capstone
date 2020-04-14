# wats-senior-captsone

## What is Whonix Automated Testing System?
* A behavior driven automated testing framework for Whonix applications and features
* Software written using python 3, behave, and dogtails

## What does WATS do?
* Automates testing of general whonix applications, features, and guis
* Allows developers to add supplemental testing features and scenarios
* Open Source

## Directory Structure:

* features - completed feature files which contain (possibly incomplete) step definitions

* stagedfeatures - completed feature files which lack completed step definitions

* plannedfeatures - incomplete feature files

## How to Use:

### Normal Installation:

### Installation for developers who want to simply use the tool:

`sudo apt-get update`

`sudo apt install whonix-debian-ats`

### Manual Installation:

`sudo apt-get update`

Make sure python 3 is installed

`python3 --version`

`sudo apt-get install python3`

from stock Whonix, first make sure you're up-to-date, then,

`sudo apt-get install python3-behave`

`sudo apt-get install python3-pip`

`sudo apt-get install python3-pyatspi`

`pip3 install dogtail` 


set up your git repository, current functionality works with merely setting it up in the home directory (does this matter?)

`git clone https://github.com/johncameronquinn/wats-senior-capstone.git`

## Related Software:
[Mycobee's Test Suite](https://github.com/Mycobee/whonix_automated_test_suite) is intended to serve as a compliment to our suite, and targets different features beyond the scope of what we could accomplish in our given time frame. However, when combined the set of testable features could be quite robust. 

## Authors:

John Quinn

Evan Tanner

Cameron Dey

## Resources:
[Whonix](https://www.whonix.org)

[Wbonix ATS Threads](https://www.whonix.org/wiki/Dev/Automated_Tests)

[Behave](https://behave.readthedocs.io/en/latest/)

[Dogtails](https://wiki.ubuntu.com/Testing/Automation/DogtailTutorial)


