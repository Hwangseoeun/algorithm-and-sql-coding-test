class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> permutation = new ArrayList<>();
        List<Integer> permutes = new ArrayList<>();

        backtracking(permutation, permutes, nums);

        return permutation;
    }

    private void backtracking(List<List<Integer>> permutation, List<Integer> permutes, int[] nums) {
        if(permutes.size() == nums.length) {
            permutation.add(new ArrayList<>(permutes));
            return;
        }

        for(int n : nums) {
            if (permutes.contains(n)) {
                continue;
            }

            permutes.add(n);

            backtracking(permutation, permutes, nums);

            permutes.remove(permutes.size() - 1);
        }
    }
}