/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        // start with headA and traverse the first list
        while (headA) {
            ListNode* cur = headB; 
            while(cur) {
                if (headA == cur) {
                    return headA; 
                }
                cur = cur-> next;
            }
            headA = headA ->next; 
        }
        return nullptr;
    }
};