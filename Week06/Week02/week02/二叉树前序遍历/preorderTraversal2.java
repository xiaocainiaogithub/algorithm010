package yiyi;

import java.util.LinkedList;


class TreeNode{
	public void Node() {}
	TreeNode val;
	private Object left;
	private TreeNode right;
	

	public LinkedList<TreeNode> preorderTraversal2 (TreeNode root){
		LinkedList<TreeNode> stack=new LinkedList<>();
		LinkedList<TreeNode> output=new LinkedList<>();
		if(root==null) {
			return output;
		}
		stack.add(root);
		while(!stack.isEmpty()) {
			TreeNode node=stack.pollLast();
			output.add(node.val);
			if(node.right!=null) {
				stack.add(node.right);
			}
			if(node.left!=null) {
				stack.add((TreeNode) node.left);
			}
		}
		return output;
	}
}