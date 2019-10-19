# namepicker
picker for waifu wars 

finallist.txt is a list converted from .csv, which we pulled from the Google Sheets. It contains names like this:
![fig.1](https://i.imgur.com/M6AbKVE.png)

my program pulls the name and adds the name to a list named namelister, where names will be appended equal to the number of tickets. For example, if a person gave 1 dollar and got 4 tickets, that person will have their name appended 4 times to the list.

In consequence, there will be as many names as there are tickets (in theory)

Then the program calculates the total number of tickets by checking the length of the list. I use a seed() and random a number between 0 and the total number of ticket to get a winning ticket number. 

Finally, I go back into namelister and look for the index of the winning ticket. Since this is a program, ticket 616 is actually the 617th ticket (a bit like cardinal vs ordinal numbers) since the first ticket has index 0.

To check for errors, I also made the program write namelister to a text file named results.txt

If there are any problems with this program, please contact me and I will check with you.
