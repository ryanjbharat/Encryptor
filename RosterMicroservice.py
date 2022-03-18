# Project - Assignment 8 Shared Microservice
# Jacob Silverberg
# silverbj@oregonstate.edu

# Instructions: Using the OverTheBoards main program, set a roster.
# Once roster is completed, select "Export Roster" button to update current roster for microservice call
# Run microservice.
# Input and save "start" in OTBMicro.txt to receive roster output in OTBMicro.txt

import time

while True:
    read_text = ""
    while read_text != "start":
        time.sleep(5)
        with open("OTBMicro.txt", "r") as infile:
            read_text = infile.readline()

    with open("roster_export.txt", "r") as infile, open("OTBMicro.txt", "w+") as outfile:
        for line in infile:
            outfile.write(line)
