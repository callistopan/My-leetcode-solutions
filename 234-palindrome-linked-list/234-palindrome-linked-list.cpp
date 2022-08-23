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
    bool isPalindrome(ListNode* head) {
        
        ListNode* prev=NULL;
        ListNode* slow=head;
        ListNode* fast=head;
        
        while (fast and fast->next){
            fast=fast->next->next;
            // reverse
            ListNode* nextt= slow->next;
            slow->next=prev;
            prev=slow;
            slow=nextt;
            
        }
        
        if (fast){
            slow=slow->next;
        }
        
        while (prev and prev->val==slow->val){
            slow=slow->next;
            prev=prev->next;
        }
        
        return !prev;
    }
};


