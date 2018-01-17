// Project Euler
// Alex Johnson
// Problem 28: Number spiral diagonals

#include <stdio.h>

int main(void) {

  int spiral_width = 1001;
  int ring_num = spiral_width / 2;

  int sum = 1;

  int i;
  for (i = 1; i <= ring_num; i++) {
    int ring_width = i * 2 + 1;
    int ring_square = ring_width * ring_width;
    int step = ring_width - 1;

    int j;
    for (j = 0; j < 4; j++) {
      sum += ring_square;
      ring_square -= step;
    }

  }

  printf("%d\n", sum);
  return 0;
}
