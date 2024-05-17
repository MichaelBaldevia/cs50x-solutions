# TODO
from cs50 import get_string

def main():
    #Get sentence
    sentence = get_string("Input a sentence/phrase: ")

    #Get reading index
    reading_index = readability_index(sentence)

    #Classify
    if reading_index <= 1:
        print("Before Grade 1")
    elif reading_index >=1 and reading_index <16:
        if reading_index > 1 and reading_index < 3:
            print("Grade 2")
        else:
            print("Grade " + str(reading_index))
    else:
        print("Grade 16+")

def readability_index(sentence):
    #Number of letters
    number_of_letter = 0
    letters = [s for s in sentence]
    c = 0
    while c < len(sentence):
        if letters[c].isalpha():
            number_of_letter += 1
        c += 1

    #Number of sentence
    number_of_sentence = (len(sentence.split('.')) - 1)  + (len(sentence.split('!')) - 1)+  (len(sentence.split('?')) - 1)

    #Number of words
    number_of_words = len(sentence.split())

    #Get Index
    index = 0.0588 * (100.00 *  number_of_letter / number_of_words ) - 0.296 * (100.00 * number_of_sentence  / number_of_words) - 15.8

    return round(index)

if __name__ == '__main__':
    main()