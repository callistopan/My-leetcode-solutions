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
    ListNode* partition(ListNode* head, int x) {
        // create two dummy nodes one for less than x and one for greater than x
        
        ListNode* less= new ListNode(-1);
        
        ListNode* t= less;
        
        ListNode* great= new ListNode(-1);
        ListNode* y = great;
        
        ListNode* curr = head;
        
        
        while (curr){
            
            if (curr->val<x){
                
                less->next=new ListNode(curr->val);
                less=less->next;
            }
            else{
                great->next=new ListNode(curr->val);
                great=great->next;
            }
            
            curr=curr->next;
        }
        
        less->next=y->next;
        
        return t->next;
        
    }
};






