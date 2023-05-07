import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

def ask_user():
    word = input('Enter a word: ').upper()
    try:
       output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Please use only letters')
        ask_user()
    else
        print(output_list)

ask_user()



