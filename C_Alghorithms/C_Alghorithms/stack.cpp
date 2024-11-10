// AutoClicker.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <ctype.h>

#define MAX_LEN 1000
#define EMPTY -1
#define FULL (MAX_LEN -1)

typedef struct stack {
    char s[MAX_LEN];
    int top;
} stack;

void reset(stack* stk) {
    stk->top = EMPTY;
}

void push(char c, stack* stk)
{
    stk->top++;   //init new top element
    stk->s[stk->top] = c; // assign values for new top element
}

char pop(stack* stk) {
    return(stk->s[stk->top--]);  // reverse to push
}
char top(stack* stk) {
    return(stk->s[stk->top]); //look at the top and get value
}

int is_empty(const stack* stk) {
    return (stk->top == EMPTY);
}

int is_full(const stack* stk) {
    return (stk->top == FULL);
}

/*
int main()
{
    stack stack_of_char;
    const char* str = "i am vitalio am i";
    char str_back[20];
    int index = 0;

    reset(&stack_of_char);
    printf("original is: %s\n", str);

    while (str[index] != '\0') {
        printf("%c\n", str[index]);
        push(str[index++], &stack_of_char);
    }
    index = 0;

    while (!is_empty(&stack_of_char) && index < 20)
        str_back[index++] = pop(&stack_of_char);

    printf("reverse is: %s\n", str_back);
    printf("\n\n");
    return 0;
}
*/
