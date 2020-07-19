package yiyi;

import java.util.Map;
import java.util.Stack;
import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class aa{
	public int val;
	public Stack() {
	}
	public void push(int x) {
		
	}
	public void pop() {
		
	}
	public boolean isEmpty() {
		return false;
	}
    TreeNode node;
    boolean status;
    public node(){
        this.node=node;
    }
    //public Node(object data, Node next) { this.Data = data; this.Next = next;

}


public class inorderTraversal {
	public List<Integer> inorderTraversal (TreeNode root){
		List<Integer> res=new ArrayList<>();
		Stack<TreeNode> Stack=new Stack<>();
		TreeNode curr=root;
		while(curr!=null||!Stack.isEmpty) {
			while(curr!=null) {
				Stack.push(curr);
				curr=curr.left;
			}
			curr=Stack.pop();
			res.add(curr.val);
			curr=curr.right;
		}
		return res;
	}
}