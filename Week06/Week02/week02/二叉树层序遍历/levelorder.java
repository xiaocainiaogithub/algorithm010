package yiyi;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import javax.swing.tree.TreeNode;



class Node{
	public Node() {}
	public Node(int _val) {
		val=_val;
	}
	public Node(int _val,List<Node> _children) {
		val= _val;
		children=_children;
	}
	public int val;
	public List<Node> children;
	public Object left;
	public TreeNode right;
	

	public void levelorder (Node root){
		List<Integer> values= new ArrayList<>();
		Queue<Node> queue=new LinkedList<>();
		queue.add(root);
		while(!queue.isEmpty()) {
			Node nextNode=queue.remove();
			values.add(nextNode.val);
			for(Node child : nextNode.children) {
				queue.add(child);
			}
		}
	}
}