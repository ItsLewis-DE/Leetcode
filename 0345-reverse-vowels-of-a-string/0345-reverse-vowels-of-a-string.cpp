
class Solution {
public:
    string reverseVowels(string s) {
        int l =0, r = s.length()-1;
        while (l<r) {
            while (l<r and !isVowel(s[l]))
                l+=1;
            while (l<r and !isVowel(s[r])) {
                r-=1;
            }
            swap(s[l],s[r]);
            l+=1;
            r-=1;
    }
        return s;
    }
    private:
        bool isVowel(char c) {
            c=  tolower(c);
            return c == 'a' || c == 'e' || c == 'i' || c=='o' ||c == 'u';
        }
};