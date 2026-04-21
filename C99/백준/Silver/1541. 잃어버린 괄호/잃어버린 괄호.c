#include <stdio.h>
#include <stdlib.h>

int main() {
    char arr[51];
    scanf("%s", arr);

    int sum = 0;
    int temp = 0;
    int minus_flag = 0;

    for(int i=0; arr[i] != '\0'; i++) {
        if(arr[i] >= '0' && arr[i] <= '9') {
            temp = temp * 10 + (arr[i] - '0');
        } 
        else {
            if(minus_flag) {
                sum -= temp;
            } else {
                sum += temp;
            }
            
            if(arr[i] == '-') minus_flag = 1;
            temp = 0;
        }
    }

    if(minus_flag) {
        sum -= temp;
    } else {
        sum += temp;
    }

   printf("%d\n", sum);
   return 0; 
}
