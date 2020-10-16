/* Date: February 12, 2019
 * Editor: Vim
 * Operating System Used: CentOS 7 Linux
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WORD_LENGTH 20
#define MAX_NUM_UNIQUE_WORDS 120
#define MAX_NUM_LINES 100
#define MAX_LINE_LENGTH 80

int index(char *t, FILE *f); /*function prototype*/

char words[MAX_NUM_UNIQUE_WORDS][MAX_LINE_LENGTH];
int new_token_counter = 1; /*keeps track of number of new words*/
int num_words = 0;
int num_lines_read_in = 0;

int index(char *t, FILE *f) {
        int i;
        int counter = 1; /*position of old word before moved to top*/

        /*if token is already in words[][]*/
        for(i=1; i<new_token_counter; i++) {
     		if(strcmp(words[i], t) == 0) {
			int c = new_token_counter-1;
			while(strcmp(words[c], t) != 0) {
                		counter++;
                        	c--;
			}	
                       	fputc((128+counter), f);
			/*implement MTF*/
			int j;
                	char temp[MAX_WORD_LENGTH];
                	memcpy(temp, words[i], MAX_WORD_LENGTH);
                	for(j=i; j<new_token_counter; j++) {
                		memcpy(words[j], words[j+1], MAX_WORD_LENGTH);
                	}
                	memcpy(words[new_token_counter-1], temp, MAX_WORD_LENGTH);
                	return i;
                }
        }
	
	/*if token is new*/
	if (i <= MAX_NUM_UNIQUE_WORDS) {
                strncpy(words[i], t, MAX_WORD_LENGTH);
                new_token_counter++;
                fputc((128+i), f);
                fputs(words[i], f);
        }
        return -1;
}

int main(int argc, char *argv[]) {
        char line[MAX_LINE_LENGTH];
	int i; /*use later to create output file name*/
	
        if(argc < 2) {
                fprintf(stderr, "Error: please type in a filename\n");
                exit(1);
        }

        FILE *input_file = fopen(argv[1], "r");
	
	/*create output file name*/
        int argument_length = strlen(argv[1]);
        char arg[argument_length];
        char *infile_name = argv[1];
        for(i=0; (arg[i]=infile_name[i]) != '\0'; i++) {
                ;
        }
        char outfile_name[strlen(arg)];
        strncpy(outfile_name, arg, strlen(arg)-3);
        strcat(outfile_name, "mtf");

        FILE *output_file = fopen(outfile_name, "w");

        /*Insert magic number at start of output file*/
        fputc(0xba, output_file);
        fputc(0x5e, output_file);
        fputc(0xba, output_file);
        fputc(0x11, output_file);

        if(input_file == NULL) {
                fprintf(stderr, "Error: cannot open file requested\n");
                exit(1);
        }

        if (output_file == NULL) {
                fprintf(stderr, "Problems opening %s for output\n", argv[1]);
                exit(1);
        }

	while(fgets(line, MAX_LINE_LENGTH+1, input_file)) { /*note that fgets reads in n-1 characters*/
		if(num_lines_read_in <= MAX_NUM_LINES) {
			int x; /*index function's return*/
                	line[strlen(line)-1] = '\0'; /*remove trailing new line*/
                	char* token = strtok(line, " ");
                	while(token != NULL) {
                        	num_words++;
                        	x = index(token, output_file);
                        	token = strtok(NULL, " ");
                	}
		}
        fputc('\n', output_file); /*encode newline character to output_file*/
	num_lines_read_in++;
	}

        fclose(input_file);
        fclose(output_file);

        return 0;
}	
