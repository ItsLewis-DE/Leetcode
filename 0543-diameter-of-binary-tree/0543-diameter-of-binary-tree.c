/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 typedef struct TreeNode TreeNode;
int diameterOfBinaryTree(struct TreeNode* root) {
    int dfs(TreeNode*root,int *res) {
        if(root==NULL) return 0;
        int sau_trai = dfs(root->left,res);
        int sau_phai = dfs(root->right,res);
        *res = fmax(*res,sau_trai+sau_phai);
        return fmax(sau_trai,sau_phai)+1;
    }
    int res =0;
    dfs(root,&res);
    return res;
}