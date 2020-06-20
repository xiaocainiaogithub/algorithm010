package yiyi;

import java.util.Map;

public class twoSum2HashMap {
	public int[] twoSum2(int[] nums, int target) {
		Map<Integer,Integer>map=new HashMap<>();
		for(int i=0;i<nums.length;i++) {
			int complement=target-nums[i];
			if(map.containsKey(complement)) {
				return new int[] {map.get(complement),i};
			}
			map.put(nums[i], i);
		}
		throw new IllegalArgumentException("No two sum solution");
	}
}
