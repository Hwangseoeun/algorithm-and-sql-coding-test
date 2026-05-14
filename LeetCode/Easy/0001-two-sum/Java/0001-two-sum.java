import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> num_list = new HashMap<>();
        List<Integer> idxs = new ArrayList<Integer>();

        for(int i=0; i<nums.length; i++) {
            int find = target - nums[i];

            if(num_list.containsKey(find)) {
                idxs.add(num_list.get(find));
                idxs.add(i);
            }
            else {
                num_list.put(nums[i], i);
            }
        }

        int[] answer = new int[idxs.size()];
        for(int i=0; i<idxs.size(); i++) {
            answer[i] = idxs.get(i);
        }

        return answer;
    }
}