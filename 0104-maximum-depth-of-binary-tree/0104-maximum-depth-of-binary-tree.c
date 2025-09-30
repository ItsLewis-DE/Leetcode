/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 typedef struct TreeNode TreeNode;
int maxDepth(struct TreeNode* root) {
    if(root==NULL) return 0;
    int dem =1;
    int dem_trai = maxDepth(root->left);
    int dem_phai = maxDepth(root->right);
    return dem+fmax(dem_trai,dem_phai);
}