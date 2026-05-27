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

    np_list['decade'] = (np_list['year'] // 10) * 10
    np_list['usa_born_winner'] = np_list['birth_country'] == 'United States of America'

    decade_usa_ratios = np_list.groupby('decade')['usa_born_winner'].mean()
    max_decade_usa = int(decade_usa_ratios.idxmax())

# QUESTION NO.3: WHICH DECADE AND NOBEL PRIZE CATEGORY COMBINATION AHD THE HIGHEST PROPORTION OF FEMALE LAUREATS?

    np_list['is_female'] = np_list['sex'] == 'Female'
    female_proportions = np_list.groupby(['decade', 'category'])['is_female'].mean()
    final_combination = female_proportions.idxmas()

    max_female_dict = {int(final_combination[0]): str(final_combination[1])}

# QUESTION NO.4: WHO WAS THE FIRST WOMAN TO RECEIVE A NOBEL PRIZE, AND IN WHAT CATEGORY?
    
    female_winners = np_list[np_list['sex'] == 'Female'].sort_values(by='year')

    first_woman_name = str(female_winners['full_name'].values[0])
    first_woman_category = str(female_winners['category'].values[0])

# QUESTION NO.5: WHICH INDIVIDUALS OR ORGANIZATIONS HAVE WON MORE THAN ONE NOBEL PRIZE THROUGHOUT THE YEARS?

    name_counts = np_list['full_name'].value_counts()
    repeat_list = list(name_counts[name_counts > 1].index)

# OUTPUTS SETTINGS

    print('=' * 100)
    print("                                     EXAM RESULTS SUMMARY                    ")
    print("=" * 100)

    print(f'# QUESTION NO.1: WHAT IS THE MOST AWARDED GENDER AND BIRTH COUNTRY')
    print(f"  • Most Awarded Gender: {top_gender}")
    print(f"  • Most Awarded Birth Country: {top_country}\n")

    print(f"QUESTION NO. 2")
    print(f"  • Decade with Highest US Ratio: {max_decade_usa}\n")

    print(f"QUESTION NO. 3")
    print(f"  • Highest Female Proportion Combo: {max_female_dict}\n")
    