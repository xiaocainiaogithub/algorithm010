package yiyi;

import java.util.LinkedList;
import java.util.List;


class TreeNode{
	public void Node() {}
	TreeNode val;
	public Object left;
	public TreeNode right;
	

	public LinkedList<TreeNode> preorderTraversal3 (TreeNode root){
		LinkedList<TreeNode> output=new LinkedList<>();
		Object node=root;
		while(node!=null) {
			if(node.left==null) {
				output.add(node.val);
				node=node.right;
			}else {
				TreeNode predecessor=node.left;
				while((predecessor.right!=null)&&(predecessor.right!=node)) {
					predecessor=predecessor.right;
				}
				if(predecessor.right==null) {
					output.add(node.val);
					predecessor.right=node;
					node=node.left;
				}else {
					predecessor.right=null;
					node=node.right;
				}
			}
		}
		return output;
	}
}