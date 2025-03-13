#include <bits/stdc++.h>

using namespace std;


bool canFinish(int numCourses, vector<vector<int>>& prerequisites) 
{
    if(prerequisites.empty()) return true;
    for(int i=0; i<prerequisites.size(); i++)
    {
        if(prerequisites[i][1] > prerequisites[i][0]) return false; 
    }

    return true;
    
}


int main()
{
    vector<vector<int>> pre;
    
    

	return 0;
}