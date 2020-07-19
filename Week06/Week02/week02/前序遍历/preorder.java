package yiyi;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

class Node{
	public int val;
	public List<Node> children;
	public Node(){}
	public Node(int _val){
		val = _val;
	}
	public Node(int val,List<Node>_children){
		val = val;
		children= _children;
	}
}

public class preorder {
	public List<Integer>preorder (Node root){
		LinkedList<Node> stack=new LinkedList<>();
		LinkedList<Integer> output=new LinkedList<>();
		if(root==null) {
			return output;
		}
		stack.add(root);
		while(!stack.isEmpty()) {
			Node node=stack.pollLast();
			output.add(node.val);
			Collections.reverse(node.children);
			for(Node item : node.children) {
				stack.add(item);
			}
		}
		return output;
	}
}