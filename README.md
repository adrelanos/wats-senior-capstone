# wats-senior-capstone
Whonix Automated Testing Suite for Team 4.1 at CofC


### Welcome to the Whonix Automated-Testing-Suite Development Repository

This wiki will operate as both information for the repository and a demo for the wiki documentation to accompany the working tool.

Demo wiki pages should be separate from the repo-specific documentation, to make publishing to the real wiki in the future easier.

***

## Installation

To avoid confusion, this installation is specifically for contributors to the testing tool's development itself. 

Installation for developers who want to simply use the tool should be different, and ideally simply:

`sudo apt install whonix-debian-ats`

However, to contribute, we will need to download dependencies. In the future, even this could be simplified to:

`sudo apt install whonix-debian-ats-dev`

As of writing, manual installation is required.

### Manual Installation

make sure python 3 is installed, our team is using python 3.7.3 .

`python3 --version`

`sudo apt-get install python3`

from stock Whonix, first make sure you're up-to-date, then,

`sudo apt-get install behave`

`sudo apt-get install python3-pip`

`pip3 install dogtail` 

`sudo apt-get install accerciser`

set up your git repository, current functionality works with merely setting it up in the home directory (does this matter?)

`git clone https://github.com/johncameronquinn/wats-senior-capstone.git`

`git checkout <branch`

