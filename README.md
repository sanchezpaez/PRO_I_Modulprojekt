Installation and functionality description
=======================

1. Intro
-------

This directory contains a framework to generate limitless text-adventure games.
The structure of the game is the following: once the game starts, the aim of the game is presented. The player is created based on the user's input, and it has a starting location. They can move around some spaces, that contain objects. The player can interact with the things around them and perform actions on them. The player has lives, that they can lose after using certain objects. If they run out of lives, they lose the game. The player needs to find, grab and use a special object in order to win the game.

The directory contains:
-An OOP framework 
-A specific game("Please the Cat").
-An example of how the game can be played.
-A UML diagram that explains relationships between objects in the framework.
-A tests.py file to run tests on all the files, and which shows an example of a simple new game.


2. Prerequisites
-------

The game was coded using Python version 3.10. It is recommended to run it on the latest version as earlier versions can be unstable.

No aditional packages need to be installed.

If you do not have Python installed:

### How to install Python

Install the version of Anaconda compatible with your operative system (Windows, Mac, linux) here: https://docs.anaconda.com/anaconda/install/index.html

3. How to use
-------
### If you want to play 'Please the Cat Game'

* Download and save the folder modulprojekt in your computer wherever you wish. Then from Terminal (look for 'Terminal' on Spotlight), or CMD for Windows,  set your working directory to that of your folder (for example: cd Desktop/modulprojekt).

```bash
cd where_you_saved_the_downloaded_folder/modulprojekt
```

* Once you are in the right working directory, type the following ('python' may be 'python3' on your computer):

```bash
python please_the_cat_main.py
```

You should see on your screen: 
'What is your name?'
>

You are ready to play!


### If you want to use the framework to make a new game

The framework contains all the necessary classes to create and run your game.
For the user to be able to make a new game the following steps need to be taken:

1) Download and save the framework directory.
2) Create new .py file and import:
  ```
  from framework.game import Game
  from framework.room import Room, SpecialRoom
  from framework.thing import InfiniteUseThing, SingleUseThing
  from framework.player import Player
  ```
3) Add/create `Thing`s & `Room`s as in the example game (`please_the_cat.py`)
4) Finalize the rooms by setting their connections like this:
  ```python
  kitchen = Room(...)
  hallway = Room(...)
  kitchen.east_room = hallway
  hallway.west_room = kitchen
  ``` 
5) Init and start your game following the example (`please_the_cat.py`).  
The tests.py file shows an example of a new implementation: the new variables for Game, Room and Thing instances (within the rooms) need to be created. The player will be generated within the game.


4. How to contribute
-------

The framework can be extended by adding more modules and methods. More scenes and challenges can be added. Don't be shy!


5. Acknowledgements
-------

paetzel-pruesmann@uni-potsdam.de for setting the minimal requirements for this PRO I module project.

6. Contact information
-------

If you have any questions or problems during they installation process, feel free to email sandrasanchezp@hotmail.com
