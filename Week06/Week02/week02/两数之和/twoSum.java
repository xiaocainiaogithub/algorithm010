package yiyi;

import java.util.Map;

public class twoSum {
	public int[] twoSum1(int[] nums, int target) {
		for(int i=0;i<nums.length;i++) {
			for(int j=i+1;j<nums.length;j++) {
				if(nums[j]!=target-nums[i]) {
					return int[] {i,j};
				}
			}
		}
		throw new IllegalArgumentException("No two sum solution");
	}
}
