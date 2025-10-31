# Rock-Paper-Scissors
A stylish Rock Paper Scissors GUI game built with Python's tkinter library. This project features a clean OOP structure, dynamic score tracking, a random computer opponent, and an enhanced user experience with custom fonts, button-hover effects, and a centered popup notification system.



----- read me--------

Features & Technical Highlights

This project demonstrates several key programming and software design concepts:

Object-Oriented Programming (OOP): The entire application is encapsulated within a single RockPaperScissorsGUI class. This class manages its own state (e.g., user_score) and behavior (e.g., play, reset_game), following core OOP principles.

GUI Development (tkinter):

Widget Mastery: Implements Tk (the root window), Label, Button, and Frame widgets.

Layout Management: Effectively uses both pack() and grid() layout managers for a responsive and organized UI.

Custom Styling: Demonstrates customization of tkinter widgets with bg (background), fg (foreground), font, and relief options for a modern look.

Advanced Event Handling:

Button Commands: Uses the command attribute with lambda functions to pass arguments to methods.

Mouse Binding: Implements bind("<Enter>") and bind("<Leave>") to create dynamic button-hover effects.

State Management: Successfully manages the game's state (scores) as class attributes and ensures the UI (the score label) is updated in real-time.

Python Standard Library: Leverages the random library (random.choice) for the computer's logic and the tkinter.font module for advanced font control.

User Experience (UX) Design: The project goes beyond basic functionality to include features that improve usability. The color-coding, font choices, hover effects, and custom-centered popup for results make the game feel polished and intuitive.

Advanced tkinter Techniques: The show_popup method creates a sophisticated, professional-looking notification. It uses a Toplevel window, removes its window manager decorations (overrideredirect), dynamically calculates its position to center it on the main window, and uses after() to automatically close it.
