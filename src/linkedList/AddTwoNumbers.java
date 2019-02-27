package linkedList;

/**
 *
 * Add two linked lists in reversed order into a third reversed linked list. The solution 
 * pattern involves simultaneously traversing two data structures and updating a third data
 * structure appropriately. 
 *
 * pseudocode: 
 * 1) Initialize a dummy node in the solution list to zero. 
 *    The solution is then incrementally appended to this dummy node. 
 * 2) Initialize the sum variable to 0.
 * 3) Use two independent pointers to crawl through each list one node at time. 
 * 4) On each iteration of the loop, use the pointers to inspect the respective nodes and 
 *    recalculate the sum of the two summands. 
 *    The sum is composed of two digits: a sum digit and a carry digit. 
 * 5) Isolate the sum by taking the remainder after division by 10. 
 *    Initialize the next node to this sum. 
 * 6) Leave the carry in the sum variable during the next iteration of the loop 
 *    by dividing the sum variable by 10. 
 */
public class AddTwoNumbers {

	public static void main(String[] args) {
		//list representing the number 21
		ListNode node1 = new ListNode(1);
		node1.next = new ListNode(2);
		node1.next.next = null;
		
		//list representing the number 43
		ListNode node2 = new ListNode(3);
		node2.next = new ListNode(4);
		node2.next.next = null;
		
		//result of adding the two lists should be 64 (printed out as 46 in reverse)
		ListNode solution = addTwoNumbers(node1, node2);
		//print solution
		printList(solution);
	}
		
		private static void printList(ListNode solution) {
			for(ListNode current = solution; current != null; current = current.next) {
				System.out.print(current.val);
			}
	}

	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	        //copy parameters into local variables
			ListNode list1 = l1;
	        ListNode list2 = l2;
	        
	        //solution list is constructed after the dummy node
	        ListNode dummyNode = new ListNode(0);
	        ListNode d = dummyNode;
	        
	        int sum = 0;
	        
	        //continue as long as either list is not null
	        while (list1 != null || list2 != null) {
	            sum /= 10;
	            //if one list is empty and the other is not, only add from the non-empty
	            //list to the sum
	            if (list1 != null) {
	                sum += list1.val;
	                //advance the pointer
	                list1 = list1.next;
	            }
	            if (list2 != null) {
	                sum += list2.val;
	                //advance the pointer
	                list2 = list2.next;
	            }
	            
	            //store the sum digit in the new node
	            d.next = new ListNode(sum % 10);
	            
	            //advance d in the solution list so that it points to the new node
	            d = d.next;
	        }
	        
	        if (sum / 10 == 1)
	            d.next = new ListNode(1);
	        return dummyNode.next;  
	    }	
	}


