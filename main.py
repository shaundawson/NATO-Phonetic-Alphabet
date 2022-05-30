import pandas

#TODO 1. Create a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict) 

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

