#include <iostream>
#include <vector>
using namespace std;

class SingleNumber {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int val : nums) {
            ans ^= val;
        }
        return ans;
    }
};

int main() {
    SingleNumber s;
    vector<int> nums = {8, 9, 3, 3, 5, 8, 9};
    cout << s.singleNumber(nums) << endl;
    return 0;
}