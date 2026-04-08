%{
#include <stdio.h>
#include <ctype.h>
%}

%%
[a-z]   { printf("%c", toupper(yytext[0])); }
.|\n    { printf("%c", yytext[0]); }
%%

int yywrap() { return 1; }

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *f = fopen(argv[1], "r");
        if (f) { yyin = f; }
    }
    yylex();
    return 0;
}