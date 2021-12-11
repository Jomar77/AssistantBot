import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\system32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'photos': "C:\\Users\\jomna\\Pictures"
}

def open_notepad():
    os.startfile(paths['notepad'])

def open_photos():
    os.startfile(paths['photos'])

def open_calculator():
    sp.Popen(paths['calculator'])