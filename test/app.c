#include <stdio.h>

int fib(int i) {
  if (i == 0 || i == 1)
    return 1;
  else
    return fib(i-1) + fib(i-2);
}

int main(void) {
  printf("%u\n", fib(40));
  return 0;
}
