#include<bits/stdc++.h>

using namespace std;

// Input: tokens = ["2","1","+","3","*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9

int evalRPN(vector<string>& tokens) 
{
    int result = 0;
    stack<string> s;
    for(int i=0; i<tokens.size(); ++i)
    {
        if(tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/")
        {
            s.push(tokens[i]);
        }
        else
        {
            int x = stoi(s.top());
            s.pop();
            int y = stoi(s.top());
            s.pop();
            if(tokens[i] == "+")
            {
                s.push(to_string(x+y));
                result=x+y;
            }
            else if(tokens[i] == "-")
            {
                s.push(to_string(y-x));
                result=y-x;
            }
            else if(tokens[i] == "*")
            {
                s.push(to_string(x*y));
                result=x*y;
            }
            else
            {
                s.push(to_string(y/x));
                result=y/x;
            }
            // cout << x << " " << y << " " << result << endl;
        }
    }

    return result;
}

int main()
{
    vector<string> s = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};

    cout << evalRPN(s);
    

    return 0;
}