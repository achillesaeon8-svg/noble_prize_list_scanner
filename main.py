import pandas as pad
import numpy as nup

def main():

    try:
        np_list = pad.read_csv('nobel.csv')
    except FileNotFoundError:
        print('Error: "nobel.csv" not found in your current folder directory')
        print('Please ensure "noble.csv" is placed in the exact same folder as the program for it to be identified and successfuly run.')
        return
    
# QUESTION NO.1: MOST AWARDED GENDER AND BIRTH COUNTRY

    gender_counts = np_list['sex'].value_counts()
    country_counts = np_list['birth_country']

    top_gender = str(gender_counts.index[0])
    top_country = str(country_counts.index[0])
