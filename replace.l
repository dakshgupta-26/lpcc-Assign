%{
#include <stdio.h>
#include <string.h>

char find_word[100];
char replace_word[100];
%}

%%
[a-zA-Z0-9_]+   {
                    if (strcmp(yytext, find_word) == 0) {
                        printf("%s", replace_word);
                    } else {
                        printf("%s", yytext);
                    }
                }
.|\n            { printf("%s", yytext); }
%%

int yywrap() { return 1; }

int main(int argc, char **argv) {
    if (argc != 4) {
        printf("Error: Missing arguments for Find/Replace.\n");
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (!f) return 1;
    yyin = f;

    strcpy(find_word, argv[2]);
    strcpy(replace_word, argv[3]);

    yylex();
    fclose(f);
    return 0;
}