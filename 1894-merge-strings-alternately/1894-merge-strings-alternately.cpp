class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        for(int i=0;i<max(word1.length(),word2.length());i++) {
            if ( i < word1.length()) {
                result = string(result) + word1[i];
            }
            if (i <word2.length()) {
                result = string(result) +word2[i];
            }
        }
        return result;
    }
};