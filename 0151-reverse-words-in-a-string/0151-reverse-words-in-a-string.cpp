class Solution {
public:
    string reverseWords(string s) {
        int fast =0 , slow =0;
        int n = s.size();
        while (fast <n && s[fast] ==' ') {
            fast +=1;
        }
        while (fast < n) {
            if (s[fast] == ' ') {
                while ((fast < n) && (s[fast] ==' ')) {
                    fast +=1;
                }
                if ((fast <n) and (s[fast] !=' '))
                    s[slow++] =' ';
            }
            else {
                s[slow++] = s[fast++];
            }
        }
        s.resize(slow);
        reverse(s.begin(),s.end());
        int start =0;
        for(int end =0;end <= s.size();end++) {
            if (end == s.size() || s[end]==' ') {
                reverse(s.begin()+ start,s.begin() +end);
                start = end +1;
            }
        }
        return s;
}   
};