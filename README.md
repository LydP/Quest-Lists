# Introduction
Most of the video games I like to play are single-player, open-world RPGs, such as the Elder Scrolls series, the Fallout 
series, The Witcher, etc. In order to get what I consider to be the best experience playing those games, I like to 
complete all available quests/missions. To do this, I'll look up all the quests that are in a game before starting 
to play it, add them to an Excel spreadsheet, and then check them off as I play through the game. This method has 
been working fine for the past few years, but it's somewhat clunky, and gets even moreso with some of the branching 
questlines available in games like Fallout: New Vegas, where some quests are mutually exclusive and others you can't 
complete if you go too far down a certain path. So, to more elegantly handle my quest lists, clean up my documents 
fold, and to provide some simple QOL improvements, I've decided to make this simple application.

# Technical
I'm creating the GUI using Qt Designer and PySide6. I'll store all data associated with the quests in SQLite3 
files, and interface with them in the application using SQLite3. So far, I'm fairly confident that writing the 
necessary queries and creating the backend logic will be straightforward. My main hurdle right now is learning Qt and 
PySide.

Otherwise, since plans change, this project is too young for me to go into further detail.

# Intended Features
* Clean interface from which to choose different quest lists and interact with them
* Quest and game searching
* Simple "mark quest completed/failed" system
* Basic statistics (quests completed, quests remaining, percent complete, etc.)
* Prerequisite tracking 
* Mutually exclusive quest tracking 
* Quest contingency tracking
* Collectibles tracking
