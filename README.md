# Hangman Game-Sanjana Maity_25BHI10104
#  - Student Project

## Project Overview
This is my project for the Introduction to Problem Solving and Programming course. I decided to build a classic "Hangman" game because I wanted to work with strings and loops. The main goal was to create a game that doesn't just run once, but actually saves your high score for next time.

## Features
* **Classic Gameplay:** You have 6 tries to guess the hidden word.
* **High Scores:** I used file handling to save the top score. If you beat the high score, it updates a file on your computer so it remembers you next time.
* **Custom Words:** Instead of hard-coding words inside the Python script, the game reads them from a text file (`words.txt`). You can add your own words there easily.
* **Error Checking:** If you type a number or a symbol by mistake, the game won't crash. It just tells you to try again.

## Technologies Used
* Python 3
* Google Colab (for writing the code)
* Git (for version control)

## How to Install and Run
1.  Download this folder to your computer.
2.  Make sure you have Python installed.
3.  Open the folder in your terminal or command prompt.
4.  Type this command: `python main.py`
5.  The game menu should appear.

## How to Test It
* **Test the Win/Loss:** Try to win a game and see if the "Victory" screen shows up. Then try to lose on purpose to see the "Game Over" screen.
* **Test Invalid Inputs:** When it asks for a letter, try typing a number like "5" or a symbol like "$". The program should warn you instead of crashing.
* **Test the Save Feature:** Win a game, close the program, and open it again. Check if your high score is still there.
