from time import sleep
import random

# Project: Shared Microservice - Custom Greeting
# ONID: macdonaw
# Resources: based off some of my code from my A2-microservice project

# greetings program will choose from - can customize by replacing any/all of the greetings
greetings = [
    "Hello",
    "Howdy",
    "Hey there",
    "Hiya",
    "'Sup",
    "Good day",
    "Welcome"
]

# loop whole check for
while True:
    # loop check the communication file for "start" command word
    command = "stop"
    while command != "start":
        # check communication file for start command
        with open('comm_file.txt', 'r') as comm_file:
            command = comm_file.readline()
            sleep(0.1)

    # once start command has been received, choose random greeting
    greeting = random.choice(greetings)

    # write greeting back out to communication file
    with open('comm_file.txt', 'w') as comm_file:
        print(greeting)
        comm_file.write(greeting)


