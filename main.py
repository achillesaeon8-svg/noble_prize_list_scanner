import pandas as pad
import numpy as nup

def main():
    try:
        np_list = pad.read_csv('nobel.csv')
    except FileNotFoundError:
        print('Error: "nobel.csv" not found in your current folder directory')
        print('Please ensure "noble.csv" is placed in the exact same folder as the program for it to be identified and successfuly run.')