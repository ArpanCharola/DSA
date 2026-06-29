// Leetcode: https://leetcode.com/problems/maximum-subarray/description/
#include <iostream>
using namespace std;

int maxSubArraySum(int arr[], int n) {
    //int max_val =INT_MIN;
    int max_val = arr[0];
    int curr_sum = arr[0];

    for (int i = 1; i < n; i++) {
        //curr_sum += arr[i];
        //if (curr_sum < 0) {
        //   curr_sum = 0;
        //}
        curr_sum = max(arr[i], curr_sum + arr[i]);
        max_val = max(max_val, curr_sum);
    }
    return max_val;
}

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "Maximum subarray sum is: " << maxSubArraySum(arr, n) << endl;
    return 0;
}