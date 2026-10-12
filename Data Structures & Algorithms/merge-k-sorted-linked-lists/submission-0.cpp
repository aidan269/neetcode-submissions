/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // create an empty list node
        vector<int> nodes; 
        // for each linked list, traverse it and append every node's value to nodes
        for (ListNode* lst : lists) {
            while (lst) {
                nodes.push_back(lst->val);
                lst = lst->next;
            }
        }
        //sort the nodes list
        sort(nodes.begin(), nodes.end());
        // create a new linked list
        ListNode* res = new ListNode(0);
        ListNode* cur = res; 
        for (int node: nodes) {
            cur->next = new ListNode(node);
            cur = cur->next;
        }
        // return the head of the new merged linked list
        return res->next;
    }
};
