class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_can = *max_element(candies.begin(),candies.end());
        vector<bool> result;
        for(auto c : candies) {
            result.push_back(c + extraCandies >= max_can);
        }
        return result;
    }
};