"""This program takes any sentence and converts it to camel case, with first word being lowercase
and first letter of subsequent words capitalized"""


def camelcase(sentence):
    word_list = sentence.split()  # turns sentence into list of words
    first_letters_capital = []  # empty list
    for word in word_list:  # loops through each word in word_list
        first_letters_capital.append(word.title())  # creates new list with first letter of each word capitalized
    list_to_single_string = ''.join(first_letters_capital)  # converts list of strings into single string and removes
    # white space - https://stackoverflow.com/questions/36094979/convert-a-list-of-strings-into-one-string
    camel_case_sentence = list_to_single_string[0].lower() + list_to_single_string[1:]  # capitalizes first letter of
    # string - https://www.geeksforgeeks.org/python-lowercase-first-character-of-string/)

    # if sentence[0].isalpha() == False
    #     print('Please use only letters')

    return camel_case_sentence


def main():
    sentence = input('Enter a sentence to convert to camelCase: ')
    output = camelcase(sentence)  # stores camelCase sentence in variable
    print(output)


main()
