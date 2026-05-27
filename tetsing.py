import pandas as pd

nobel_df= pd.read_csv("nobel.csv")

#TOP GENDER--------------------------------------------------------------------------------
gender_counter=nobel_df["sex"].value_counts()
#if "Male" < "Female": does not count the values of male and female
if gender_counter['Male'] < gender_counter["Female"]:
    top_gender=("The Gender with the most Nobel prizes is the Female Gender")
else:
    top_gender=("The Gender with the most Nobel prizes is the Male Gender")
print(top_gender)
#TOP COUNTRY--------------------------------------------------------------------------------
country_measure=nobel_df["birth_country"].value_counts()
top_country=country_measure.idxmax()
print(f"The country with the most Nobel prizes is: {top_country}")

#MAX DECADE USA--------------------------------------------------------------------------------
nobel_df["decade"] = (nobel_df["year"] // 10) * 10
usa_born=nobel_df[nobel_df["birth_country"]=="United States of America"]
# decade_counts = usa_born["decade"].value_counts().sort_index()
# top_decade = decade_counts.idxmax() 
# top_count = decade_counts.max()
usa_per_decade = usa_born.groupby("decade").size()
total_per_decade = nobel_df.groupby("decade").size()
# max_decade_usa=(f"The decade with the most USA born Nobel Prize Winners: {top_decade}\nNumber of USA born Nobel Prize Winners from all categories: {top_count}")
usa_ratio = usa_per_decade / total_per_decade
max_decade_usa = int(usa_ratio.idxmax()) #Store as integer
usa_count = int(usa_per_decade[max_decade_usa]) #counts max winners and stores as int
print(f"The decade with the most USA born Nobel Prize Winners: {max_decade_usa}")
print(f"Number of USA born Nobel Prize Winners from that decade: {usa_count}")

#MAX FEMALE DICT--------------------------------------------------------------------------------
nobel_df["decade"]=(nobel_df["year"]//10)*10
female_laur=nobel_df[nobel_df["sex"]=="Female"]
female_per_decade=female_laur.groupby(["decade","category"]).size()
top_female_per_decade=female_per_decade.idxmax()
max_female_dict={int(top_female_per_decade[0]):str(top_female_per_decade[1])}
print(max_female_dict)

#FIRST WOMAN NAME--------------------------------------------------------------------------------
female_identifier=nobel_df[nobel_df["sex"]=="Female"]
sort_first_woman=female_identifier.sort_values("year")
first_woman_name=sort_first_woman.iloc[0]["full_name"]
print(first_woman_name)
#FIRST WOMAN CATEGORY--------------------------------------------------------------------------------
first_woman_category=sort_first_woman.iloc[0]["category"]
print(first_woman_category)

#REPEAT LIST--------------------------------------------------------------------------------
appearance_counter=nobel_df["full_name"].value_counts()
# repeat_list=list((appearance_counter[appearance_counter >=2]).items())
repeat_list = list(appearance_counter[appearance_counter >= 2].index)
print(repeat_list)