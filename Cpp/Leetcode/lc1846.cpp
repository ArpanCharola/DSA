//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class lc1846 {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int ans = 1;

        for ( int i = 1; i < arr.size(); i++ ) {
            if(arr[i] >= ans + 1){
                ans++;
            }
        }
        return ans;
    }
};

int main() {
    lc1846 solution;
    vector<int> arr = {1, 2, 5, 6, 9, 3, 11, 34, 2, 3};
    cout << solution.maximumElementAfterDecrementingAndRearranging(arr) << endl;
    return 0;
}