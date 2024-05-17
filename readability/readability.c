#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int readability_index(string sentence);

int main(void)
{
    int reading_index = 0;
    string sentence = get_string("Input a sentence/words/phrase: ");
    reading_index = readability_index(sentence);

    if (reading_index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (reading_index >= 1 && reading_index < 16)
    {
        if (reading_index > 1 && reading_index <= 3) {
            printf("Grade 2\n");
        }
        else
        {
            printf("Grade %i\n", reading_index);
        }
    }
    else
    {
        printf("Grade 16+\n");
    }
}

int readability_index(string sentence) {

    int number_of_letter = 0;
    int number_of_sentence = 0;
    int number_of_words = 1;
    float index = 0;

    for (int i = 0, n = strlen(sentence) ; i < n ; i++)
    {
        if (isalpha(sentence[i]))
        {
            number_of_letter++;
        }
        else if (ispunct(sentence[i]))
        {
            if (sentence[i] == '.' || sentence[i] == '?' || sentence[i] == '!')
            {
                number_of_sentence++;
            }
        }
        else if (sentence[i] == ' ')
        {
            number_of_words++;
        }
    }

    index = 0.0588 * (100.00 * (float) number_of_letter / (float) number_of_words ) - 0.296 * (100.00 * (float) number_of_sentence  / (float) number_of_words) - 15.8;

    return roundf(index);
}