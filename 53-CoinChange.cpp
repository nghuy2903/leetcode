#include <bits/stdc++.h>

using namespace std;


int coinChange(vector<int>& coins, int amount) {
        // Khởi tạo mảng DP
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0; // Cần 0 coin để đạt được tổng tiền là 0

        // Tính toán DP
        for (int i = 1; i <= amount; ++i) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
            cout << dp[i] << " ";
        }

        // Trả về kết quả
        return dp[amount] > amount ? -1 : dp[amount];
    }

int main()
{

    vector<int> coint = {4,2,5};

    cout << coinChange(coint, 11);

    return 0;
}