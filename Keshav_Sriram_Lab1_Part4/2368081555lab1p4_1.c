#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Hash-table-like struct for
// tallying occurrences of words
// partially based on https://www.tutorialspoint.com/data_structures_algorithms/hash_table_program_in_c.htm
struct WordFreq {
   char word[255];   
   int occurrence;
};

int main ()
{
	// File I/O variables
	FILE *infile;
	FILE *outfile;

	// Buffer for word length, assume words are
	// no more than 254 letters long
	char buff[255];
	// Store words, assuming that there are no
	// more than 500 unique words
	struct WordFreq dict[500];
	// Count the number of words
	int num_words=0;

	// C file IO
	infile = fopen("in.txt", "r");
	// If file is not empty
	if (infile) {
		// Read the file word by word
		// from here: https://stackoverflow.com/questions/3463426/in-c-how-should-i-read-a-text-file-and-print-all-strings
		while (fscanf(infile, "%s", buff)!=EOF)
		{
			// Lowercase string from here:
			// https://stackoverflow.com/questions/2661766/how-do-i-lowercase-a-string-in-c
			for(int i = 0; buff[i]; i++){
				buff[i] = tolower(buff[i]);
			}
			// Check new word alongside each word
		  	for(int dict_idx = 0; dict_idx <= num_words; ++dict_idx)
		  	{
		  		// If the loop reaches the end of
		  		// the dictionary
			  	if(dict_idx == num_words)
			  	{
			  		// Put the new word in the empty
			  		// dictionary slot
			  		strcpy(dict[num_words].word, buff);
			  		dict[num_words].occurrence=1;
			  		++num_words;
			  		break;
			  	}
			  	// If the two strings match,
			  	// then increment the occurrence
			  	if(!strcmp(buff, dict[dict_idx].word))
			  	{
			  		++dict[dict_idx].occurrence;
			  		break;
			  	}
		  	}
		}
		fclose(infile);
	}

	// print all the words to an output file
	outfile = fopen("out.txt", "w+");

	for(int dict_idx = 0; dict_idx < num_words; ++dict_idx)
   {
    	fprintf(outfile, "The word %s occurred %d time(s).\n",dict[dict_idx].word,dict[dict_idx].occurrence);
   }

   fclose(outfile);

	return 0;
}