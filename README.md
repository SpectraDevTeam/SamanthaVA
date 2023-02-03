# Samantha Voice Assistant

All of the Samantha code for her Voice Assistant! A fully functional (Kind of, Still a WIP) voice assistant with many commands! This is the basic version of Sam. I have made all of this. This is all my hard work and I care about it a lot. Please use with care. Any modifications to code on main branches should be approved by me. 


## Installation
***
Download with ```git clone https://github.com/SpectraDevTeam/SamanthaVA``` in the folder where you would like to have her. Install dependencies with ```pip install -r requirements.txt``` in the main folder (There has been problems with requirement installation, Requirements are as follows: google, pygame, playsound, pyttsx3, requests, speechrecognition, and textblob. I would suggest using [Anaconda](https://www.anaconda.com/products/distribution "Anaconda Home") for the installation and running of the program)
<br /><br />
Before running her you will want to use ```python3 checkvoices.py``` to check what voices are on your system. As this is still in the testing phase the Final voice is not yet availible. you will want to select one of the voices from the ones generated and it will edit voice.txt to run the voice you select.

## Running the Program
***
Before running her you will want to use ```python3 checkvoices.py``` to check what voices are on your system and select one for use. As this is still in the testing phase the Final voice is not yet availible. you will want to select one of the voices from the ones generated and it will edit voice.txt to run the voice you select.
<br /><br />
To Run the voice assistant run ```python3 main.py``` or use one of the executable files (**WIP, NOT YET AVAILABLE**) made for your operating system.

## Using the Program
***
**Throughout her use Keep your eyes on your terminal, there are intervals where she will be processing and cannot hear you. The terminal tells you when she is not listening and is processing.** 
<br /><br />
You can start the command proccess by using her wakeup word! "Sam" will wake her up and have her listen for commands. There is a gap between the wakeup word and the command input so remember to watch the terminal The Program has a specific list of commands you can use. It will try to guess what command you meant if the command you use is not in the list and is similar to one that is in the list.
<br /><br />
**COMMAND LIST:**
* end - shuts down the program
* flip - flips a coin
* joke - tells a joke
* roll - rolls a dice based on a specified number
* timer - sets a timer for a specified time
* time - tells the time
* add - adds multiple numbers
* subtract - subracts multiple numbers
* multiply - multiplies multiple numbers
* divide - divides multiple numbers
* search - searches google for a prompt
* image - searches google images for a prompt
* app - opens an app on your computer

![Code Size](https://img.shields.io/github/languages/code-size/SpectraDevTeam/SamanthaVA_ML) ![]()
