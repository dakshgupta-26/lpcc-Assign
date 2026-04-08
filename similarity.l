%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <strings.h>

char wordsA[2000][100];
int countA = 0;
int matchCount = 0;
int pass = 1;

// Function to check stop words
int isStopWord(char *w) {
    char *stops[] = {"is", "am", "a", "the", "if", "and", "of", "to", "in", "it", "that", "for", "on", "with", "as", "this", "was", "at", "by", "an", "be", "from", "or", "are", "etc"};
    int n = sizeof(stops)/sizeof(stops[0]);
    for(int i=0; i<n; i++) {
        if(strcasecmp(w, stops[i]) == 0) return 1;
    }
    return 0;
}
%}

%%
[a-zA-Z]+   {
                if (pass == 1) {
                    if (!isStopWord(yytext)) {
                        strcpy(wordsA[countA++], yytext);
                    }
                } else {
                    for(int i=0; i<countA; i++) {
                        if(strcasecmp(wordsA[i], yytext) == 0) {
                            matchCount++;
                            break; // word found in A
                        }
                    }
                }
            }
.|\n        { /* ignore special characters and spaces */ }
%%

int yywrap() { return 1; }

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Error: Provide Document A and Document B\n");
        return 1;
    }

    FILE *fa = fopen(argv[1], "r");
    if (!fa) { printf("Cannot open File A\n"); return 1; }
    yyin = fa; pass = 1; yylex(); fclose(fa);

    FILE *fb = fopen(argv[2], "r");
    if (!fb) { printf("Cannot open File B\n"); return 1; }
    yyin = fb; pass = 2; yylex(); fclose(fb);

    float percentage = 0.0;
    if (countA > 0) percentage = ((float)matchCount / countA) * 100.0;

    printf("Total valid words in Doc A: %d\n", countA);
    printf("Matching words in Doc B: %d\n", matchCount);
    printf("Similarity Score: %.2f%%\n", percentage);

    if (percentage >= 40.0) {
        printf("\nRESULT: SIMILAR (>= 40%% Match)\n");
    } else {
        printf("\nRESULT: NOT SIMILAR (< 40%% Match)\n");
    }
    return 0;
}