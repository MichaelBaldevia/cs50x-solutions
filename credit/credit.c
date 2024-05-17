#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

long credit_card_number;
int credit_card_length;

int main(void)
{
    do
    {
        credit_card_number = get_long("What's your credit card number? ");
        long credit_card_number_container = credit_card_number;


        while (credit_card_number_container > 0) {
            credit_card_number_container = credit_card_number_container / 10;
            credit_card_length++;
        }

        int number[credit_card_length], originallength[credit_card_length];

        for (int i = 0; i < credit_card_length; i++)
        {
            number[i] = credit_card_number % 10;
            credit_card_number = credit_card_number / 10;
        }

        for (int i = 1; i < credit_card_length; i++) {
            originallength[i] = number[i];
        }

        for (int i = 1; i < credit_card_length; i+=2) {
            number[i] = number[i] * 2;
        }


        int countsum = 0;
        int temp;

        for (int i = 0; i < credit_card_length; i++)
        {
            temp = (number[i] % 10) + (number[i]/10 % 10);
            countsum = countsum + temp;
        }

        if (((originallength[12] == 4 && credit_card_length == 13) || (originallength[15] == 4 && credit_card_length == 16)) && countsum  % 10 == 0 )
        {
            printf("VISA\n");
        }
        else if (originallength[14] == 3 && (originallength[13] == 4 || originallength[13] == 7) && countsum  % 10 == 0  && credit_card_length == 15)
        {
            printf("AMEX\n");
        }
        else if (originallength[15] == 5 && (originallength[14] == 1 || originallength[13] == 2 || originallength[13] == 3 || originallength[13] == 4 || originallength[13] == 5)&& countsum  % 10 == 0 &&  credit_card_length == 16)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    while (credit_card_number < 0);
    
}