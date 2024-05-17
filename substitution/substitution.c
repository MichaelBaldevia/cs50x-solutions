#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

char LETTERS[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
string encryption;

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key \n");
        return 1;
    }

    encryption = argv[1];
    char key[strlen(argv[1])];
    int alphabet  = sizeof(LETTERS) / sizeof(char);
    int crawler = 0;
    string plaintext;

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        key[i] = toupper(encryption[i]);
    }

    for (int i = 0, n = strlen(argv[1]); i < n ;  i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Usage: ./substitution key \n");
            return 1;
        }
        if (key[i] == key[i+1])
        {
            printf("Usage: ./substitution key \n");
            return 1;
        }
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    plaintext = get_string("Plaintext: ");
    char ciphertext[strlen(plaintext)];

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        for (int x = 0; x < alphabet ; x++)
        {
            if (toupper(plaintext[crawler]) == LETTERS[x])
            {
                if (islower(plaintext[crawler]))
                {
                    ciphertext[crawler] = tolower(key[x]);
                    crawler++;
                }
                else
                {
                    ciphertext[crawler] = key[x];
                    crawler++;
                }
            }
            else if (!isalpha(plaintext[crawler]) && crawler <  strlen(plaintext) )
            {
                ciphertext[crawler] = plaintext[crawler];
                crawler++;
            }
        }
    }

    printf("ciphertext: ");

    for (int i = 0,n = strlen(plaintext); i < n; i++)
    {
        printf("%c", ciphertext[i]);
    }

    printf("\n");
}