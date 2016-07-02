import os
import time

#width of the console
WIDTH = 79


message = "HELLO"
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line
#banner display equivalents. each letter in the dictionary
#maps to 7 strings, one for each line of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "E" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               
               "H" : [ "*   *",
                       "*   *",
                       "*   *",
                       "*****",
                       "*   *",
                       "*   *",
                       "*   *" ], 

               "O" : [ "*****",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*****" ],

               "L" : [ "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*    ",
                       "*****" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               
               }


#display is carried for each vharacter in the message  line by line
for row in range(7):
    for char in message:
        printedMessage[row]+=(str(characters[char][row])+" ")

#offset is how far to the right we want to print
        offset = WIDTH
while True:
    os.system("cls")
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.1)
