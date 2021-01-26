#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 1
day = 26

def test_code():
    assert main.lastLetter("a") == "a", 'lastLetter("a") == "a" failed'
    assert main.lastLetter("climb") == "b", 'lastLetter("climb") == "b" failed'

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
