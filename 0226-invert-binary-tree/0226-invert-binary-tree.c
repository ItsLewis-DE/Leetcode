/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 typedef struct TreeNode TreeNode;
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root == NULL) return NULL;
    TreeNode *temp = root->right;
    root->right = root->left;
    root->left =temp;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}