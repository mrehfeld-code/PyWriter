from time import sleep
from sys import stdout

def printn(text):
    stdout.write(text)

def write(text = "Hello world!"):
    for i in range(0, len(text)):
        printn(text[i])
        sleep(0.25)

    printn("\n")
