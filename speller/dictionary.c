// Implements a dictionary's functionality

#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

unsigned int hash_value;
unsigned int word_count;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //Get current hash of the word
    int index = hash(word);

    node *current_word = table[index];

    //loop in the dictionary to check if the word is existing
    while (current_word != NULL)
    {
        if(strcasecmp(current_word -> word, word) == 0)
        {
            return true;
        }
        current_word = current_word -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int value = 0;
    unsigned int word_length = strlen(word);
    for (int i = 0; i < word_length; i++)
    {
        value = value + 37 * toupper(word[i]);
    }
    value = value % N;
    return value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{

    //Load Dictionary
    FILE *word_dictionary = fopen(dictionary, "r");
    //File can't be opened
    if (word_dictionary == NULL)
    {
        return false;
    }
    //Longest Word possible
    char longest_word[LENGTH + 1];

    // Scan dict for strings that are not the end of the file
    while (fscanf(word_dictionary, "%s", longest_word) != EOF)
    {
        // Allocate memory for new node
        node *n = malloc(sizeof(node));
        // If malloc returns NULL, return false
        if (n == NULL)
        {
            return false;
        }
        // Pointer to next node and word itself
        strcpy(n->word, longest_word);
        // Hash the word to get hash value
        hash_value = hash(longest_word);
        // Get new word pointer
        n->next = table[hash_value];
        // Set head to new pointer
        table[hash_value] = n;
        //add to the total word count
        word_count++;
    }
// Close dictionary
    fclose(word_dictionary);
// Dictionary load is successful
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // return total number of word
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //Loop in the table, pass the pointer and free the current
    for (int i = 0; i < N; i++)
    while (table[i] != NULL)
    {
        node *tmp = table[i] ->next;
        free(table[i]);
        table[i] = tmp;
    }
    return true;
}
