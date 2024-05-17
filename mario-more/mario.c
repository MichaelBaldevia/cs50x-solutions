#include <cs50.h>
#include <stdio.h>

int pyramid_height;
void pyramid_generator(void);

int main(void)
{
    do
    {
        pyramid_height = get_int("How high is the pyramid? ");
    }
    while (pyramid_height <= 0 || pyramid_height > 8);
    pyramid_generator();

}

void pyramid_generator()
{
    //Pyramid height
    for (int j = 0; j < pyramid_height; j++)
    {
        //print left spaces
        for (int k = pyramid_height - 1; k > j; k--)
        {
            printf(" ");
        }

        //print left pyramid
        for (int l = 0; l <= j; l++)
        {
            printf("#");
        }

        //print gap
        printf("  ");

        //print right pyramid
        for (int x = 0; x <= j; x++)
        {
            printf("#");
        }
        printf("\n");
    }
}