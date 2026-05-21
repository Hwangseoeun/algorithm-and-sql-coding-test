class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> combination = new ArrayList<>();
        
        result.add(new ArrayList<>(combination));

        for(int i=0; i<nums.length; i++) {
            combination.add(nums[i]);
            result.add(new ArrayList<>(combination));
            recursion(result, combination, nums, i);
            combination.remove(combination.size() - 1);
        }

        return result;
    }

    private void recursion(List<List<Integer>> result, List<Integer> combination, int[] nums, int idx) {
        for(int i=idx+1; i<nums.length; i++) {
            combination.add(nums[i]);
            result.add(new ArrayList<>(combination));

            recursion(result, combination, nums, i);

            combination.remove(combination.size() - 1);
        }
    }
}