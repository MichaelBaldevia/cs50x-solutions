#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    BYTE buffer[512];
    int BUFER_SIZE = 512;
    int output_counter = 0;
    FILE *image_start = NULL;
    char output[8];

    while (fread(&buffer, BUFER_SIZE, 1, input))
    {
        //JPEG header start
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //if start of new jpeg then close the current
            if (output_counter != 0)
            {
                fclose(image_start);
            }
            //Open new file for new image
            sprintf(output, "%03i.jpg", output_counter);
            image_start = fopen(output, "w");
            output_counter++;
        }
        
        //Image found then save image
        if  (output_counter != 0)
        {
             fwrite(&buffer, BUFER_SIZE, 1, image_start);
        }
    }
        fclose(input);
        fclose(image_start);
        return 0;
}