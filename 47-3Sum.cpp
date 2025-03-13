#include <bits/stdc++.h>

using  namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<vector<int>> levelOrder(TreeNode* root) 
{
    vector<vector<int>> result;
    if(root == nullptr) return result;

    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty())
    {
        int level = q.size();
        vector<int> temp;
        for(int i=0; i<level; i++)
        {
            TreeNode* p = q.front();
            temp.push_back(p->val);

            if(p->left) q.push(p->left);
            if(p->right) q.push(p->right);
        }

        result.push_back(temp);
    }

    return result;
}





int main()
{
    vector<int> nums = {1,-1,-1,0};//-1 -1 0 1

   

    
    return 0;
}
