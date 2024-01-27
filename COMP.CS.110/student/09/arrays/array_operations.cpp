#include "array_operations.hh"

int greatest_v1(int *itemptr, int size)
{
    int greatest = *itemptr;
    for (int i = 1; i < size; i++) {
        if (*(itemptr + i) > greatest) {
            greatest = *(itemptr + i);
        }
    }
    return greatest;
}

int greatest_v2(int *itemptr, int *endptr)
{
    int size = (endptr - itemptr);
    int greatest = *itemptr;
    for (int i = 1; i < size; i++) {
        if (*(itemptr + i) > greatest) {
            greatest = *(itemptr + i);
        }
    }
    return greatest;
}

void copy(int* itemptr, int* endptr, int* targetptr)
{
    int size = endptr - itemptr;
    for (int i = 0; i < size; i++) {
        *(targetptr + i) = *(itemptr + i);
    }
}

void reverse(int* leftptr, int* rightptr)
{
    int size = rightptr - leftptr;
    for (int i = 0; i < size / 2; i++) {
        int temp = *(leftptr + i);
        *(leftptr + i) = *(rightptr - i - 1);
        *(rightptr - i - 1) = temp;
    }
}
