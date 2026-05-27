import pandas as pad
import numpy as nup

def main():

    try:
        np_list = pad.read_csv('nobel.csv')
    except FileNotFoundError:
        print('Error: "nobel.csv" not found in your current folder directory')
        print('Please ensure "noble.csv" is placed in the exact same folder as the program for it to be identified and successfuly run.')
        return
    
# QUESTION NO.1: WHAT IS THE MOST AWARDED GENDER AND BIRTH COUNTRY

    gender_counts = np_list['sex'].value_counts()
    country_counts = np_list['birth_country']

    top_gender = str(gender_counts.index[0])
    top_country = str(country_counts.index[0])

# QUESTION NO.2: WHICH DECADE HAD THE HIGHEST RATIO OF US-BORN NOBEL PRIZE WINNERS TO TOTAL WINNERS IN ALL CATEGORIES?

# QUESTION NO.3: WHICH DECADE AND NOBEL PRIZE CATEGORY COMBINATION AHD THE HIGHEST PROPORTION OF FEMALE LAUREATS?

# QUESTION NO.4: WHO WAS THE FIRST WOMAN TO RECEIVE A NOBEL PRIZE, AND IN WHAT CATEGORY?

# QUESTION NO.5: WHICH INDIVIDUALS OR ORGANIZATIONS HAVE WON MORE THAN ONE NOBEL PRIZE THROUGHOUT THE YEARS?