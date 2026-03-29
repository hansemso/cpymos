// cpymos/cpp/score.c
#include <stdio.h>

int calculate_score(int *durations, int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += durations[i];
    }
    return total;
}