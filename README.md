# HangMan

Install Tkinter and Pillow modules before running the program
In cmd console, change directory to the drive on which Python is installed and type:
- pip install tkinter
- pip install pillow

Line 92: play() function 
gets a list of characters of a random word by calling letters() function of an user-defined module.
Returns two lists:
-letters_list containing the letters, this will be used to check for the letters
-changing_list containing the required no. of blanks, this list will eventually be used to get a string of blanks & correctly guessed letters

Line 99: lw() function
takes a list as argument & returns a string containing the elements of list seperated by space
this string will be used to display blanks & correctly guessed letters

Line 105: The Stage
Setting up the interface

Line 112: Fonts
Defining fonts to be used later

Line 123: Resources
Importing images using PIL module

Line 139: Display
Creating a Canvas for displaying various objects

Line 143: Title Screen
Displaying the contents of title screen
-the Button's action is set to execute a function game_start() on clicking

Line 8: game_start() function
executed on clicking the Start button
    Lines 9-17 & 86-88: Gameplay Screen
    Deleting contents of title screen
    Getting letters_list & changing_list
    Displaying contents of gameplay screen
        -Entry Box (ebox) is set to execute a func enter_click() on pressing Enter Key
    Line 88:
    defining a list 'entered' to store the entered alphabets
    Lines 37-83: enter_click() func
    assigning value to variable 'text' depending on different easy_to_understand conditions
    'text' is displayed at the end of execution of function
    - In case of Winning (Word completely guessed) or Losing (out of guesses),
        game_restart_prep() function is called
    Lines 19-35: game_restart_prep() func
    deletes the entry box and instruction
    displays a 'Play Again' button which is set to execute game_restart() function on clicking
        Lines 23-27: game_restart() func
        deletes everything on screen (except bg)
        calls the game_start() function
