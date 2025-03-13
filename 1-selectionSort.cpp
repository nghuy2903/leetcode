// Input Output
// 4 
// 5 7 3 2 
// Buoc 1: 2 7 5 3 
// Buoc 2: 2 3 7 5 
// Buoc 3: 2 3 5 7

#include <bits/stdc++.h>
using namespace std;

void selectionSort(int a[], int n) {
    for(int i=0; i<n-1; i++) {
        int temp = i;
        for(int j=i+1; j<n; j++) {
            if(a[j] < a[temp]) {
                temp = j;
            }
        }
        swap(a[i], a[temp]);
        cout << "Buoc " << i+1 << ": ";
        for(int k=0; k<n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

void interchangeSort(int a[], int n) {
    for(int i=0; i<n-1; i++) {
        for(int j=i+1; j<n; j++) {
            if(a[i] > a[j]) {
                swap(a[i], a[j]);
            }
        }
        cout << "Buoc " << i+1 << ": ";
        for(int k=0; k<n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

void insertionSort(int a[], int n) {
    for(int i=1; i<n; i++){
        int key = a[i];
        int j = i-1;
        while(j>=0 && a[j] > key) {
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = key;
        cout << "Buoc " << i << ": ";
        for(int k=0; k<n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

int main() {
    int a[5] = {5, 7, 3, 2};
    // selectionSort(a, 4);
    // interchangeSort(a, 4);
    insertionSort(a, 4);
    return 0;
}
