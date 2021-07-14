#include<stdio.h>
#define MAX 9999

int main(){
    int n;
    scanf("%d", &n);
    int array[n];
    for(int i = 0 ; i < n ; i ++){
        scanf("%d", &array[i]);
    }
    int count_not_positive = 0;
    int flag[MAX];
    for(int i = 1; i < MAX ; i ++){
        flag[i] = false;
    }
    for(int i = 0 ; i < n ; i ++){
        if (array[i] > 0){
            flag[array[i]] = true; // Đánh dấu các số dương đã có trong mảng
        }
        else{
            count_not_positive += 1;
        }
    }
    if (count_not_positive == n){
        printf("1"); // Nếu tất cả các số trong mảng đều âm
    }
    else{
        for(int i = 1 ; i < MAX; i ++){
            if (flag[i] == false){
                printf("%d", i); // số dương nhỏ nhất chưa được đánh dấu
                break;
            }
        }
    }
}
