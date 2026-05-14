import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        List<Integer> idxs = new ArrayList<Integer>();

        for(int i=0; i<nums.length-1; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    idxs.add(i);
                    idxs.add(j);
                }
            }
        }

        int[] answer = new int[idxs.size()];
        for(int i=0; i<idxs.size(); i++) {
            answer[i] = idxs.get(i);
        }

        return answer;
    }
}