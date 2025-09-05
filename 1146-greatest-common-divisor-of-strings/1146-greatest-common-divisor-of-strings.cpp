int ucln(int a,int b) {
            if (b==0)
                return a;
            return ucln(b,a%b);
        }
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int len_kq = ucln(str1.length(),str2.length());
        string candidate = str1.substr(0,len_kq);
        string temp1 = "";
        for(int i =0;i<str1.length()/len_kq;i++) {
            temp1 += candidate;
        }
        string temp2 = "";
        for(int i =0;i< str2.length()/len_kq;i++) {
            temp2 += candidate;
        }
        if ((str1 == temp1) && (str2 == temp2))
            return candidate;
        else {
            return "";
        }
    }
};